#!/bin/bash
api_key="$1"
city_id=118743
url="https://api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&cnt=5&units=metric&lang=en"
curl ${url} -s -o /home/ryan/dotfiles/conky/scripts/weather.json
