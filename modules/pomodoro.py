import time
import winotify
import json

def save_stats(stats):
    try:
        with open("data/stats.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    history.append(stats)

    with open("data/stats.json", "w") as f:
        json.dump(history, f, indent=4)

def breaktime(minutes):
    if minutes == "":
        minutes = 25
    duration = int(minutes * 60)
    end_time = time.monotonic() + duration
    print(f"Starting a {minutes} minute break...\nGo outside, take a break, enjoy the sun!")
    try:
        while True:
            remaining = max(0, int(end_time - time.monotonic() + 0.999))
            mins, secs = divmod(remaining, 60)
            print(f"\r Break time remaining: {mins:02d}:{secs:02d}", end="", flush=True)
            if remaining == 0:
                break
            time.sleep(min(0.2, remaining))
        print("\nBreak time is over! Get back to work!")
        winotify._notify(title="Pomodoro Timer", message="Break time is over! Get back to work!", duration="long")
        start(25)
    except KeyboardInterrupt:
        print("\nOh well, time is lost, you can go back to work!")

def start(minutes):
    duration = int(minutes * 60)
    end_time = time.monotonic() + duration
    print(f"Starting a {minutes} minute Pomodoro session...")
    try:
        while True:
            remaining = max(0, int(end_time - time.monotonic() + 0.999))

            mins, secs = divmod(remaining, 60)

            print(f"\r Time remaining: {mins:02d}:{secs:02d}", end="", flush=True)

            if remaining == 0:
                break


        print("\nPomodoro session complete!")
        save_stats({"last_session": time.time(), "duration": minutes})

        winotify._notify(title="Pomodoro Timer", message="Time's up! Take a break.", duration="long")
    except KeyboardInterrupt:
        print("\nYou cancelled it with Ctrl+C. Next time, don't do that, I'm always watching...")