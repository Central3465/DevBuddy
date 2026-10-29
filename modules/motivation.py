import random
from datetime import datetime
import json
import os
import requests

current_date = datetime.now().strftime("%Y-%m-%d")

def fetchmotivation():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]["q"]

def checkfile():
    file = "data/motivation.json"
    dirname = os.path.dirname(file)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    return file

def ui():
    show()

def show():
    file = checkfile()
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if data == {}:
            data = {"date": "", "quote": ""}
    if data.get("date") == current_date:
        print("You have reached your daily motivation limit. Come back tomorrow!\n")
        print(f"Today's motivation was: {data.get('quote')}")
        return
    motivation = fetchmotivation()
    data = {"date": current_date, "quote": motivation}
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(motivation)
