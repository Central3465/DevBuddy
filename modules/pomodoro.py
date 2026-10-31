import time
import winotify

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

            time.sleep(min(0.2, remaining))

        print("\nPomodoro session complete!")

        winotify._notify(title="Pomodoro Timer", message="Time's up! Take a break.", duration="long")
    except KeyboardInterrupt:
        print("\nYou cancelled it with Ctrl+C. Next time, don't do that, I'm always watching...")