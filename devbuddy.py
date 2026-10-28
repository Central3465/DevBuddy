import argparse
import os

from modules.todo import loadtodo, edittodoui
from modules.codex import ui
from modules.motivation import ui

terminal_size = os.get_terminal_size() 
width = terminal_size.columns # because os.get_terminal_size() returns a tuple object

def main():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to DevBuddy!".center(width))
    print("Your personal developer toolkit.".center(width))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

    parser = argparse.ArgumentParser( prog= "devbuddy", description="Your personal dev toolkit.")

    parser.add_argument( "tool", choices=["todo", "codex", "give-me-motivation"], help="Tool you want to use...")

    args = parser.parse_args()

    if args.tool == "todo":
        loadtodo()
        edittodoui()
    elif args.tool == "codex":
        ui()
    elif args.tool == "give-me-motivation":
        ui()

if __name__ == "__main__":
    main()