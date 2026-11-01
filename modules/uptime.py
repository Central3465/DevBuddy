import requests

def check(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code, response.ok, response.elapsed.total_seconds(), response.headers, response.cookies
    except requests.exceptions.RequestException:
        return False