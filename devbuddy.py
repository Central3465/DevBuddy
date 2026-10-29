import argparse
import os

from modules.todo import loadtodo, edittodoui
from modules import codex, motivation
from modules.getcommit import get_commit

terminal_size = os.get_terminal_size() 
width = terminal_size.columns # because os.get_terminal_size() returns a tuple object

def main():
    print("-" * width)
    print("Welcome to DevBuddy!".center(width))
    print("Your personal developer toolkit.".center(width))
    print("-" * width)

    parser = argparse.ArgumentParser( prog= "devbuddy", description="Your personal dev toolkit.")

    parser.add_argument( "tool", choices=["todo", "codex", "give-me-motivation", "version"], help="Tool you want to use...")

    args = parser.parse_args()

    if args.tool == "todo":
        loadtodo()
        edittodoui()
    elif args.tool == "codex":
        codex.ui()
    elif args.tool == "give-me-motivation":
        motivation.ui()
    elif args.tool == "version":
        sha = get_commit()
        print(f"devbuddy version: {sha}")

if __name__ == "__main__":
    main()