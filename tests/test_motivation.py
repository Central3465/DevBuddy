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
    def boom(*args, **kwargs):
        return FakeResponse({"error": "You have exceeded your daily limit."}, status_code=429)
    monkeypatch.setattr(motivation.requests, "get", boom)
    motivation.show()
    out = capsys.readouterr().out
    assert "old quote" in out    