
from utils import fetch_json, get_date, get_arrow
from formats import format_forecast, format_weather


def get_location_id(location_name, weathers_json):
    for location in weathers_json:
        if location["name"] == location_name:
            return location["lid"]

def get_weather(location_id, weathers_json):
    for location in weathers_json:
        if location["lid"] == location_id:
            return location["weather"]

def get_forecast(location_id, forecasts_json):
    for location in forecasts_json:
        if location["location_id"] == location_id:
            return location["forecast"]

def main():
    ip_info = fetch_json("https://ipinfo.io/json")
    weathers_json = fetch_json("https://ws.smn.gob.ar/map_items/weather")
    forecasts_json = fetch_json("https://ws.smn.gob.ar/forecast")

    location_name = ip_info["city"]
    location_id = get_location_id(location_name, weathers_json)

    weather = get_weather(location_id, weathers_json)
    forecast = get_forecast(location_id, forecasts_json)

    print(format_weather(location_name, weather))
    print()
    print(format_forecast(location_name, forecast, "1"))

main()
