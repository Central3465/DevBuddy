import json
import os

file = "data/todo.json"

def checkfile():
    dirname = os.path.dirname(file)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump([], f)


def readfile():
    checkfile()
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def writefile(todos):
    checkfile()
    with open(file, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)


def printtodos(todos):
    if not todos:
        print("none found")
        return
    for i in todos:
        status = "x" if i.get("done") else " "
        print(f"[{status}] {i['id']} {i['task']}")


def loadtodo():
    todos = readfile()
    if not todos:
        print("none")
    else:
        printtodos(todos)
    return todos


def edittodoui():
    while True:
        print("\nCommands:")
        print(" [c] complete  [e] edit  [d] delete  [a] add  [q] quit [s] show\n")
        choice = input("Enter command: ").strip().lower()

        todos = readfile()

        if choice == "e":
            try:
                toid = int(input("edit id: "))
            except ValueError:
                print("invalid id")
                continue
            for i in todos:
                if i["id"] == toid:
                    new_task = input(f"new task [{i['task']}]: ").strip()
                    if new_task:
                        i["task"] = new_task
                        writefile(todos)
                        print(f"updated #{toid}")
                    else:
                        print("cancelled")
                    break
            else:
                print(f"todo #{toid} not found")

        elif choice == "d":
            try:
                toid = int(input("delete id: "))
            except ValueError:
                print("invalid id")
                continue
            before = len(todos)
            todos = [i for i in todos if i["id"] != toid]
            if len(todos) == before:
                print(f"no todo with id {toid}")
            else:
                writefile(todos)
                print(f"deleted: {toid}")

        elif choice == "a":
            task = input("new task: ").strip()
            if not task:
                print("cancelled")
                continue
            newid = max((i["id"] for i in todos), default=0) + 1
            todos.append({"id": newid, "task": task, "done": False})
            writefile(todos)
            print(f"added #{newid}: {task}")

        elif choice == "q":
            return

        elif choice == "s":
            printtodos(todos)

        elif choice == "c":
            todos = readfile()

            try:
                idtodo = int(input("ID of the todo you want to complete: "))
            except ValueError:
                print("invalid id")
                continue
            
            for i in todos:
                if i["id"] == idtodo:
                    if i["done"]:
                        print("already completed")
                    else:
                        i["done"] = True
                        writefile(todos)
                        print(f"completed todos #{idtodo}")
                    break
                else:
                    print(f"No todoo found with ID {idtodo}")

        else:
            print("unknown cmd")