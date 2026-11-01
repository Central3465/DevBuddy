import subprocess

def get_git_status():
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"error: {e.stderr.strip()}"

get_git_status()