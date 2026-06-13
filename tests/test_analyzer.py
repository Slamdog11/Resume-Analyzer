import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resume_Analyzer')))

import analyzer


def test_find_missing_keywords_basic():
    resume = "Python Java SQL"
    jd = "Python C++ SQL"

    missing = analyzer.find_missing_keywords(resume, jd)

    assert 'c++' in [w.lower() for w in missing]
    assert 'python' not in [w.lower() for w in missing]
    assert 'sql' not in [w.lower() for w in missing]
