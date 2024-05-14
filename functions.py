import requests

API_KEY = "94dd38bf3fb5ab6310819a999d2bc8c2"

def get_data(place, days):
    url = ("http://api.openweathermap.org/data/2.5/forecast?q="
           f"{place}&units=metric&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * int(days)
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__ == "__main__":
    print('working')


