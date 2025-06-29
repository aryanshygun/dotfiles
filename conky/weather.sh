#!/bin/bash

# Rasht, Iran city ID: 118743
api_key="7820059c007100bf460e9135ec1d7bf7"
city_id="118743"
units="metric"
lang="en"

url="https://api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&units=${units}&lang=${lang}"

mkdir -p ~/.cache
curl -s "$url" -o weather.json
