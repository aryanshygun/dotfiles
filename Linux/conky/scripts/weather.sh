#!/bin/bash
api_key=$(cat "$(dirname "$0")/.weather_api")
city_id=118743
url="https://api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&cnt=5&units=metric&lang=en"
curl ${url} -s -o /home/ryan/dotfiles/Linux/conky/scripts/weather.json
