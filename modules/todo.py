import json

def load_todo():
    with open("data/todo.json", "r") as file:
        tododata = json.load(file)
    print(tododata)

    