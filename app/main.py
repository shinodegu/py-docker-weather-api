from __future__ import print_function
import os
import requests


api_key = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(f"https://api.weatherapi.com/"
                            f"v1/current.json?key={api_key}&q=Paris&aqi=no")
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
