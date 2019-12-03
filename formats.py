import textwrap

def format_description(description):
    a = textwrap.wrap(description, 50)
    b = [textwrap.indent(x, '  ') for x in a]
    return '\n'.join(b)

def format_forecast(location_name, forecast, delta_day):
    return( f'{get_date(delta_day)}\n'
            f'{forecast[delta_day]["temp_max"]}° / {forecast[delta_day]["temp_min"]}°\n'
            f'Morning:\n{format_description(forecast[delta_day]["morning"]["description"])}\n'
            f'Afternoon:\n{format_description(forecast[delta_day]["morning"]["description"])}'
            f'\n')

def format_weather(location_name, weather):
    return (f'{location_name}\n'
            f'{weather["description"]}\n'
            f'{weather["tempDesc"]}\n'
            f'{weather["wing_deg"]} {weather["wind_speed"]} km/h')
