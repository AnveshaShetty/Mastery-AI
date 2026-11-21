"""Core tutoring loop: diagnose -> explain -> check -> adapt -> mastery."""
from . import llm, prompts

PASS_MARK = 0.67  # fraction correct needed to count as mastered


def _ctx(topic: dict, level: str, language: str) -> str:
    return (
        f"Subject: {topic['subject']}\nTopic: {topic['name']}\n"
        f"Reference notes: {topic.get('notes', '')}\n"
        f"Learner level: {level}\nLanguage: {language}"
    )


def diagnose(topic: dict, level: str, language: str, n: int = 3) -> list[dict]:
    data = llm.ask_json(prompts.DIAGNOSE.format(n=n), _ctx(topic, level, language))
    return data["questions"]


def explain(topic: dict, level: str, language: str, gaps: list[str]) -> str:
    user = _ctx(topic, level, language) + f"\nLearner's gaps: {gaps or 'none found'}"
    return llm.ask(prompts.EXPLAIN, user)


def make_check(topic: dict, level: str, language: str, previous: list[str], n: int = 3) -> list[dict]:
    system = prompts.CHECK.format(n=n, previous=previous)
    return llm.ask_json(system, _ctx(topic, level, language))["questions"]


def grade(questions: list[dict], chosen: list[int]) -> dict:
    """Graded in code (not by the model) so results are reliable."""
    correct = [q["answer_index"] == c for q, c in zip(questions, chosen)]
    score = sum(correct) / len(questions) if questions else 0.0
    missed = [q["concept_tested"] for q, ok in zip(questions, correct) if not ok]
    return {"score": score, "mastered": score >= PASS_MARK, "missed": missed, "correct": correct}


def re_explain(topic: dict, level: str, language: str, missed: list[str]) -> str:
    system = prompts.REEXPLAIN.format(missed=missed)
    return llm.ask(system, _ctx(topic, level, language))
