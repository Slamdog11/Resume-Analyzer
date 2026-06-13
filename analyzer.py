import re

def find_missing_keywords(resume_text, jd_text):

    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())

    missing = jd_words - resume_words

    return list(missing)[:20]