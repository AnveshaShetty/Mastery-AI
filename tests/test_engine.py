from tutor.engine import grade

QS = [
    {"answer_index": 1, "concept_tested": "a"},
    {"answer_index": 0, "concept_tested": "b"},
    {"answer_index": 2, "concept_tested": "c"},
]


def test_all_correct_is_mastered():
    r = grade(QS, [1, 0, 2])
    assert r["mastered"] and r["score"] == 1.0 and r["missed"] == []


def test_failing_lists_missed_concepts():
    r = grade(QS, [0, 0, 0])
    assert not r["mastered"] and r["missed"] == ["a", "c"]
