import requests
import datetime

API_KEY = "94dd38bf3fb5ab6310819a999d2bc8c2"

def get_data(place, days, kind):
    url = ("http://api.openweathermap.org/data/2.5/forecast?q="
           f"{place}&units=metric&appid={API_KEY}")

    response = requests.get(url)
    data = response.json()

    nr_values = 8 * int(days)
    filtered_data = data['list'][:nr_values]

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", '2', "Sky"))




