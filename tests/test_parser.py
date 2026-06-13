import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resume_Analyzer')))

import parser as parser_mod


def test_extract_text(monkeypatch):
    class FakePage:
        def __init__(self, text):
            self._text = text

        def extract_text(self):
            return self._text

    class FakePdf:
        def __init__(self, pages):
            self.pages = pages

    def fake_reader(file):
        return FakePdf([FakePage("Hello"), FakePage("World")])

    monkeypatch.setattr(parser_mod, 'PdfReader', fake_reader)

    text = parser_mod.extract_text(None)

    assert "Hello" in text
    assert "World" in text
