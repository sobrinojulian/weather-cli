import urllib.request
import json


def fetch_json(url):
    res = urllib.request.urlopen(url)
    _bytes = res.read()
    _str = _bytes.decode("utf-8")
    _json = json.loads(_str)
    return _json

def get_location_id(location_name, weather_json):
    for location in weather_json:
        if location["name"] == location_name:
            return location["lid"]

def get_weather(location_id, weather_json):
    for location in weather_json:
        if location["lid"] == location_id:
            return location["weather"]

def get_forecast(location_id, forecast_json):
    for location in forecast_json:
        if location["location_id"] == location_id:
            return location["forecast"]

def filter_forecast(forecast):
    d = {}
    for k, v in forecast.items():
        d[k] = {
            "date": forecast[k]["date"],
            "temp_max": forecast[k]["temp_max"],
            "temp_min": forecast[k]["temp_min"],
            "morning_description": forecast[k]["morning"]["description"],
            "afternoon_description": forecast[k]["afternoon"]["description"]
        }
    return d


def main():
    ipinfo_json = fetch_json("https://ipinfo.io/json")
    weather_json = fetch_json("https://ws.smn.gob.ar/map_items/weather")
    forecast_json = fetch_json("https://ws.smn.gob.ar/forecast")

    name = ipinfo_json["city"]
    location_id = get_location_id(name, weather_json)

    weather = get_weather(location_id, weather_json)
    forecast = get_forecast(location_id, forecast_json)
    forecast = filter_forecast(forecast)
    print(json.dumps(weather, indent=2, sort_keys=True))

    print(json.dumps(forecast, indent=2, sort_keys=True))

main()
