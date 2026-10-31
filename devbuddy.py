import argparse
import os

from modules.todo import loadtodo, edittodoui
from modules import codex, motivation
from modules.getcommit import get_commit
from modules.pomodoro import start
from modules.commitgenerator import run

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

    parser.add_argument( "tool", choices=["todo", "codex", "give-me-motivation", "version", "pomodoro", "commit"], help="Tool you want to use...")

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

if __name__ == "__main__":
    main()