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

def edittodoui():
    print("\nCommands:")
    print(" [e] edit  [d] delete  [a] add  [q] quit")
    choice = input("Enter command:").strip().lower()

    todos = loadtodo()

    if choice == "e":
        try:
            toid = int(input("edit id: "))
        except ValueError:
            print("invalid id")
            return
        for i in todos:
            if i["id"] == toid:
                new_task = input(f"new task [{i['task']}]:").strip()
                if new_task:
                    i["task"] = new_task
                    writefile(todos)
                    print(f"updated #{toid}")
                return
        print(f"todo #{toid} not found")
    elif choice == "d":
        try:
            toid = int(input("delete id: "))
        except ValueError:
            print("invalid id")
            return
        before = len(todos)
        todos = [i for i in todos if i['id'] != toid]
        if len(todos) == before:
            print(f"no todo with id {toid}")
        else:
            writefile(todos)
            print(f"deleted: {toid}")
    elif choice == "q":
        return
    elif choice == "a":
        task = input("new task: ").strip()
        if not task:
            print("cancelled")
            return
        newid = max((i["id"] for i in todos), default=0) + 1
        todos.append({"id": newid, "task": task, "done": False})
        writefile(todos)
        print(f"added #{newid}: {task}")
    else:
        print("unknown cmd")