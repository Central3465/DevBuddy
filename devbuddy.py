import argparse
import os

from modules.todo import load_todo

terminal_size = os.get_terminal_size() 
width = terminal_size.columns # because os.get_terminal_size() returns a tuple object

def main():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to DevBuddy!".center(width))
    print("Your personal developer toolkit.".center(width))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

    parser = argparse.ArgumentParser( prog= "devbuddy", description="Your personal dev toolkit.")

    parser.add_argument( "tool", choices=["todo", "checklist", "stats", "ai-chat"], help="Tool you want to use...")

    args = parser.parse_args()

    if args.tool == "todo":
        load_todo()

if __name__ == "__main__":
    main()