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

def print_forecast(forecast):
    l = []
    for k, v in sorted(forecast.items()):
        l.append({
            "date": forecast[k]["date"],
            "temp_max": forecast[k]["temp_max"],
            "temp_min": forecast[k]["temp_min"],
            "morning_description": '\n'.join(forecast[k]["morning"]["description"].split('. ')),
            "afternoon_description": '\n'.join(forecast[k]["afternoon"]["description"].split('. '))
        })
    for day in l:
        if l[0] == day: continue
        print(  f'{day["date"]}\n'
                f'{day["temp_max"]}° / {day["temp_min"]}°\n'
                f'{day["morning_description"]}\n'
                f'{day["afternoon_description"]}'
                f'\n')

def format_weather(location_name, weather):
    return (f'{location_name}\n'
            f'{weather["description"]}\n'
            f'{weather["tempDesc"]}\n'
            f'{weather["wing_deg"]} {weather["wind_speed"]} km/h')

def main():
    ipinfo_json = fetch_json("https://ipinfo.io/json")
    weather_json = fetch_json("https://ws.smn.gob.ar/map_items/weather")
    forecast_json = fetch_json("https://ws.smn.gob.ar/forecast")

    location_name = ipinfo_json["city"]
    location_id = get_location_id(location_name, weather_json)

    weather = get_weather(location_id, weather_json)
    forecast = get_forecast(location_id, forecast_json)

    print(format_weather(location_name, weather))
    print()
    print_forecast(forecast)
    #print(json.dumps(weather, indent=2, sort_keys=True))
    #print(json.dumps(forecast, indent=2, sort_keys=True))

main()
