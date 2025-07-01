#!/bin/bash
api_key=7820059c007100bf460e9135ec1d7bf7
city_id=118743

url="api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&cnt=5&units=metric&lang=en"
curl ${url} -s -o scripts/weather.json
