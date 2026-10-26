import json
import os

file = "data/todo.json"

def checkfile():
    os.makedirs(os.path.dirname(file), exist_ok=True)
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)

def readfile():
    checkfile()
    with open(file, "r") as f:
        return json.load(f)

def writefile(todos):
    with open(file, "w") as f:
        json.dump(todos, f, indent=2)

def printtodos(todos):
    if not todos:
        print("none found")
        return
    for i in todos:
        status = "x" if i.get("done") else " "
        print(f"{status} {i['id']} {i['task']}")

def loadtodo():
    with open(file, "r") as f:
        todos = json.load(f)

    if not todos:
        print("none")
        return

    for todo in todos:
        print(f"[{'x' if todo['done'] else ' '}] {todo['id']} {todo['task']} ")