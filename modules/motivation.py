import random
from datetime import datetime
import json
import os

current_date = datetime.now().strftime("%Y-%m-%d")

motivation = [
    "Want that Framework laptop or Apple iPad from Terra? If so, then get coding bucko!",
    "Your mind isn't working if you just doomscroll all day.",
    "Your github profile heatmap isn't going to grow unless you actually commit.",
    "Come on, what are you doing? GEt coding!",
    "You can do it!"
]

file = "data/motivation.json"

def ui():
    show()

def show():
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if data == {}:
            data = {"date": "", "quote": ""}
    if data.get("date") == current_date:
        print("Come back tomorrow!")
        return
    poo = random.randint(0, len(motivation) - 1)
    quote = motivation[poo]
    data = {"date": current_date, "quote": quote}
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(quote)
