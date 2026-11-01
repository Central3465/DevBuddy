import argparse
import os

from modules.todo import loadtodo, edittodoui
from modules import codex, motivation
from modules.getcommit import get_commit
from modules.pomodoro import start
from modules.commitgenerator import run
from modules.uptime import check
from modules.env import list, scan 
from modules.dependanalyse import find_dependencies, scan_txt, scan_toml
from modules.explain import explain_code, explain_error
from modules.weather import get_weather
from modules.uuid import generate_uuid
from modules.base64 import encode, decode

def get_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def main():
    width = get_width()
    print("-" * width)
    print("Welcome to DevBuddy!".center(width))
    print("Your personal developer toolkit.".center(width))
    print("-" * width)

    parser = argparse.ArgumentParser( prog= "devbuddy", description="Your personal dev toolkit.")

    parser.add_argument( "tool", choices=["todo", "codex", "give-me-motivation", "version", "pomodoro", "commit", "uptime", "env", "analyse", "explain", "weather", "uuid", "base64"], help="Tool you want to use...")

    args = parser.parse_args()

    if args.tool == "todo":
        loadtodo()
        edittodoui()
    elif args.tool == "codex":
        codex.ui()
    elif args.tool == "give-me-motivation":
        motivation.ui()
    elif args.tool == "pomodoro":
        user = input("How long do you want your session? (in minutes): ")
        start(int(user))
    elif args.tool == "analyse":
        print("Scanning for dependencies...\n")

        files = find_dependencies(".")

        if not files:
            print("No dependency files found.")
            return

        for file in files:
            if file.endswith(".txt"):
                scan_txt(file)
            elif file.endswith(".toml"):
                scan_toml(file)
    elif args.tool == "explain":
        question = input("What do you want the ai to do? (explain code or explain error): ")
        if question.lower() == "explain code":
            code = input("Please paste the cod here:\n")
            explanation = explain_code(code)
            print("\nExplanation:\n")
            print(explanation)
        elif question.lower() == "explain error":
            error = input("paste the error here:\n")
            explanation = explain_error(error)
            print("\nExplanation:\n")
            print(explanation)
    elif args.tool == "weather":
        city = input("Enter the city name: ")
        data = get_weather(city)
        print(data)
    elif args.tool == "uptime":
        url = input("URL to check uptime: ")
        print("Checking\n", url)
        result = check(url)
        if result:
            status_code, ok, elapsed, headers, cookies = result
            print(f"Status code: {status_code}\n")
            print(f"OK: {ok}\n")
            print(f"Time to fetch: {elapsed} seconds\n")
            print(f"Headers: {headers}\n")
            print(f"Cookies: {cookies}")
        else:
            print("failed to fetch url")
    elif args.tool == "env":
        list()
        scan()
    elif args.tool == "commit":
        commitmsg = run()
        if commitmsg:
            print("generated commit message:\n")
            print(commitmsg)
        else:
            print("could not generate commit message")
    elif args.tool == "version":
        sha = get_commit()
        if sha:
            print(f"devbuddy version: {sha}")
        else:
            print("could not fetch version (unlikely error to get so i probably broke something)")
    elif args.tool == "uuid":
        option = input("Choose UUID method: (random, time, name): ")
        print(generate_uuid(option))
    elif args.tool == "base64":
        action = input("encode or decode? (e/d): ")
        if action.lower() == "e":
            text = input("text to encode: ")
            print(encode(text))
        elif action.lower() == "d":
            text = input("text to decode: ")
            print(decode(text))
        else:
            print("innvalid action")

if __name__ == "__main__":
    main()