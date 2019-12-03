import urllib.request
import json

def fetch_json(url):
    res = urllib.request.urlopen(url)
    _bytes = res.read()
    _str = _bytes.decode("utf-8")
    _json = json.loads(_str)
    return _json

def get_date(delta_day):
    if delta_day == "0": return "0"
    if delta_day == "1": return "1"
    if delta_day == "2": return "2"
    if delta_day == "3": return "3"
    if delta_day == "4": return "4"

def get_arrow(name):
    if name == "Norte": return "Today"
    if name == "Sur": return "Today"
    if name == "Este": return "Today"
    if name == "Oeste": return "Today"
    if name == "Noreste": return "Today"
    if name == "Noroeste": return "Today"
    if name == "Sureste": return "Today"
    if name == "Suroeste": return "Today"
