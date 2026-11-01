import requests

def get_weather(city):
    if not city.strip():
        return "City name cannot be empty."

    headers = {
        "User-Agent": "DevBuddy/1.0"
    }

    try:
        url = "https://nominatim.openstreetmap.org/search"

        response = requests.get(
            url,
            params={"city": city, "format": "json"},
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        if not data:
            return "City not found."

        lat = data[0]["lat"]
        lon = data[0]["lon"]

    except requests.exceptions.Timeout:
        return "Timed out, try again later."

    except requests.exceptions.RequestException as e:
        return f"Geocoding request failed: {e}"

    except requests.exceptions.JSONDecodeError:
        return "Invalid response from geocoding service."

    try:
        url = "https://api.open-meteo.com/v1/forecast"

        response = requests.get(
            url,
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
            },
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return "Timed out, try again later."

    except requests.exceptions.RequestException as e:
        return f"Weather request failed: {e}"

    except requests.exceptions.JSONDecodeError:
        return "Invalid response from weather service."
