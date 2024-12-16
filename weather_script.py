import requests

def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "your_api_key_here"
    city = "Mumbai"
    weather_data = fetch_weather("64ebeea618bd6496526eed3d784cd3b7", city)
    if weather_data:
        print(weather_data)
    else:
        print("Failed to fetch weather data")