import time
import winotify

def start():
    session = 25 * 60
    print(f"Starting a {session // 60} minute pomodoro session...")
    while session > 0:
        print(session)
        print(f"Minutes remaining: {session // 60}")
        session -= 1
        time.sleep(1)
    else:
        print("Time's up! Take a break.")
        winotify._notify(title="DevBuddy Pomodoro", message="Time's up! Take a break.", duration="long")