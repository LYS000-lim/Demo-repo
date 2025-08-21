import requests
import json

# base_url = "https://pokeapi.co/api/v2/"
#
# def get_poke_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retreive data {response.status_code}")
#
# pokemon_name = "pikachu"
# pokemon_info = get_poke_info(pokemon_name)
#
# if pokemon_info:
#     print(f"Name: {pokemon_info["name"]}")
#     print(f"ID: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")

# def get_stock_data():
#     url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         fetch = data["Meta Data"]["3. Last Refreshed"]
#         price = data["Time Series (5min)"][fetch]["1. open"]
#         return price
#     else:
#         return None
#
# price = get_stock_data()
# symbol = "IBM"
# if price is not None:
#     print(f"{symbol}: {price}")
# else:
#     print("Failed to retrieve data")

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        articles = response.json().get("articles",[])

        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}")