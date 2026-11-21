"""Streamlit UI. Run from repo root: streamlit run app/app.py"""
import json
import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tutor import engine, storage  # noqa: E402

TOPICS = json.loads((Path(__file__).resolve().parent.parent / "content/topics.json").read_text())["topics"]
MAX_ROUNDS = 3

st.set_page_config(page_title="Mastery-ai", page_icon="🎓")
st.title("🎓 Mastery-ai")
st.caption("It only moves on when you've proven you understand.")

s = st.session_state
s.setdefault("stage", "setup")
s.setdefault("round", 0)
s.setdefault("asked", [])


def radio_quiz(questions, key):
    chosen = []
    for i, q in enumerate(questions):
        pick = st.radio(q["question"], q["options"], index=None, key=f"{key}-{i}")
        chosen.append(q["options"].index(pick) if pick else None)
    return chosen


if s.stage == "setup":
    s.learner = st.text_input("Your name")
    topic = st.selectbox("Topic", TOPICS, format_func=lambda t: f"{t['subject']} - {t['name']}")
    s.level = st.selectbox("Your level", ["beginner", "intermediate", "advanced"])
    s.language = st.selectbox("Explain in", ["English", "Kannada", "Hindi", "Tulu (simple)", "Tamil", "Telugu"])
    if st.button("Start") and s.learner:
        s.topic = topic
        with st.spinner("Preparing diagnostic..."):
            s.diag = engine.diagnose(topic, s.level, s.language)
        s.asked += [q["question"] for q in s.diag]
        s.stage = "diagnose"
        st.rerun()

elif s.stage == "diagnose":
    st.subheader("Step 1: Where are you stuck?")
    chosen = radio_quiz(s.diag, "diag")
    if st.button("Submit") and None not in chosen:
        res = engine.grade(s.diag, chosen)
        storage.save_attempt(s.learner, s.topic["name"], "diagnostic", res["score"], res["mastered"])
        with st.spinner("Writing your explanation..."):
            s.explanation = engine.explain(s.topic, s.level, s.language, res["missed"])
        s.stage = "explain"
        st.rerun()

elif s.stage == "explain":
    st.subheader("Step 2: Explanation")
    st.markdown(s.explanation)
    if st.button("I'm ready for the check"):
        with st.spinner("Preparing check questions..."):
            s.check = engine.make_check(s.topic, s.level, s.language, s.asked)
        s.asked += [q["question"] for q in s.check]
        s.round += 1
        s.stage = "check"
        st.rerun()

elif s.stage == "check":
    st.subheader(f"Step 3: Prove it (round {s.round})")
    chosen = radio_quiz(s.check, f"check{s.round}")
    if st.button("Submit answers") and None not in chosen:
        s.result = engine.grade(s.check, chosen)
        storage.save_attempt(s.learner, s.topic["name"], f"check{s.round}", s.result["score"], s.result["mastered"])
        s.stage = "result"
        st.rerun()

elif s.stage == "result":
    r = s.result
    st.metric("Score", f"{int(r['score'] * 100)}%")
    if r["mastered"]:
        st.success("Mastered! You've shown you understand this topic.")
    elif s.round >= MAX_ROUNDS:
        st.warning(f"Not yet. Revisit: {', '.join(r['missed'])}")
    else:
        st.info(f"Not yet. Let's try a different explanation. Missed: {', '.join(r['missed'])}")
        if st.button("Re-explain"):
            with st.spinner("Trying a new angle..."):
                s.explanation = engine.re_explain(s.topic, s.level, s.language, r["missed"])
            s.stage = "explain"
            st.rerun()
    if st.button("Start over"):
        for k in list(s.keys()):
            del s[k]
        st.rerun()
