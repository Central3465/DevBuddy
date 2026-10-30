import json
import pytest
from modules import motivation

@pytest.fixture(autouse=True)
def patched_file(tmp_path, monkeypatch):
    testfile = tmp_path / "test_motivation.json"
    monkeypatch.setattr(motivation, "file", lambda: str(testfile))
    return testfile

class FakeResponse:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    def json(self):
        return self.payload

def test_daily_limit(monkeypatch, capsys):
    today = motivation.current_date
    with open(motivation.checkfile(), "w", encoding="utf-8") as f:
        json.dump({"date": today, "quote": "Old quote"}, f)

    def boom(*a, **k):
        return AssertionError("should not fetch new quote when limit reahed")

    monkeypatch.setattr(motivation.requests, "get", boom)
    motivation.show()
    out = capsys.readouterr().out
    assert "old quote" in out    