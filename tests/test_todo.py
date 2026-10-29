import json
import pytest
from modules import todo

@pytest.fixture(autouse=True)

def patched_file(tmp_path, monkeypatch):
    testfile = tmp_path / "test_todo.json"
    testfile.write_text(json.dumps([]))
    monkeypatch.setattr(todo, "file", str(testfile))
    return testfile

def check_empty_list():
    assert todo.readfile() == []

def write_file():
    todos = [{ "id": 1, "task": "Test task", "done": False }]
    todo.writefile(todos)
    assert todo.readfile() == todos

def printtodosempty(capsys):
    todo.printtodos([])
    assert "none found" in capsys.readouterr().out

def loadtodosprintitems(capsys):
    todo.writefile([{ "id": 1, "task": "Test task", "done": False}])
    todo.loadtodo()
    out = capsys.readouterr().out
    assert "test task" in out