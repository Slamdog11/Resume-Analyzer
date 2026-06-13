import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resume_Analyzer')))

import ats_score


def test_calculate_score_identical_documents():
    score = ats_score.calculate_score("python java sql", "python java sql")
    assert score == 100.0


def test_calculate_score_different_documents():
    score = ats_score.calculate_score("python java", "c++ go")
    # score should be a float between 0 and 100
    assert isinstance(score, float)
    assert 0.0 <= score <= 100.0
