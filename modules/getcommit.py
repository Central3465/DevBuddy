import requests 

def get_commit():
    url = "https://api.github.com/repos/Central3465/DevBuddy/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        if commits:
            latest = commits[0]
            sha = latest.get("sha")
    return sha