import json
import os
import datetime
from winotify import Notification, audio

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
        print(f"[{status}] {i['id']} {i['task']} (priority: {i.get("priority", "medium")}) (due: {i.get("due_date", "none")})")


def loadtodo():
    todos = readfile()
    if not todos:
        print("none")
    else:
        printtodos(todos)
    return todos

def notify_todo():
    todos = readfile()
    for i in todos:
        if not i.get("done") and i.get("due_date"):
            due_date = datetime.datetime.strptime(i["due_date"], "%Y-%m-%d").date()
            today = datetime.date.today()
            if due_date == today:
                notification = Notification(app_id="DevBuddy", title="Todo Reminder", msg=f"Task '{i['task']}' is due today!", duration="short")
                notification.set_audio(audio.Default, loop=True)
                notification.show()

def edittodoui():
    while True:
        print("\nCommands:")
        notify_todo()
        print(" [c] complete  [e] edit  [d] delete  [a] add  [q] quit [s] show [cd] clear done\n")
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
                    new_task = input(f"new task [{i['task']}] (type none to skip): ").strip()
                    priority = input(f"new priority [{i.get('priority', 'medium')}]: ").strip().lower()
                    if new_task:
                        if new_task.lower() == "none":
                            new_task = i["task"]
                        i["task"] = new_task
                        if priority in ["medium", "high", "low"]:
                            i["priority"] = priority
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
            priority = input("priority (medium, high, low): ").strip().lower()
            due_date = input("due date (YYYY-MM-DD) (optional): ").strip()
            if not task:
                print("cancelled")
                continue
            if priority not in ["medium", "high", "low"]:
                print("invalid priority, defaulting to medium")
                priority = "medium"
            if due_date:
                try:
                    datetime.datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("invalid date format, ignoring...")
                    due_date = None
            else:
                due_date = None
            newid = max((i["id"] for i in todos), default=0) + 1
            todos.append({"id": newid, "task": task, "done": False, "priority": priority, "due_date": due_date})
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

        elif choice == "cd":
            todos = readfile()
            todos = [i for i in todos if not i["done"]]
            writefile(todos)
            print("cleared done todos")

        else:
            print("unknown cmd")