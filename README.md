# Mastery Tutor 🎓

> An AI tutor that finds where a student is stuck, explains it in their language and level, and only moves on once they pass a short check of understanding.

Built for **Homingo Hack Days 2026**, Track C3: *A tutor for every learner* (LLM apps).

## The problem
Most learning apps keep people busy; they don't prove anyone learned. A great personal tutor finds the exact gap, explains it your way, and keeps going until you get it. Almost nobody has one.

## How it works
1. **Diagnose**: 3 short questions locate the learner's misconception.
2. **Explain**: the LLM explains the topic at the learner's level, in their language, targeting their gaps.
3. **Check**: fresh questions (never repeats) test real understanding.
4. **Adapt**: if they fail, the tutor re-explains differently. Max 3 rounds.
5. **Proof**: grading is done in code (not by the LLM), and every attempt is stored, giving a measurable mastery result.

## Who it's for
Engineering students stuck on a concept in one subject (v1 subject: _TODO_).

## Quick start
```bash
git clone <your-repo-url> && cd mastery-ai
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # add your ANTHROPIC_API_KEY
streamlit run app/app.py
```
Run tests: `pytest`

## Project structure
```
app/app.py          Streamlit UI (stage-by-stage flow)
tutor/llm.py        Claude API wrapper
tutor/prompts.py    All prompts
tutor/engine.py     Diagnose / explain / check / grade logic
tutor/storage.py    SQLite attempt history
content/topics.json Topics and reference notes
docs/               Plan, AI tools, team split
tests/              Unit tests
```

## AI tools, models and libraries
See [docs/AI_TOOLS.md](docs/AI_TOOLS.md).

## Team
- Anvesha U Shetty
- Pratham Pal

## Status
Work in progress. See [docs/TEAM_PLAN.md](docs/TEAM_PLAN.md).
