import json

import requests


def main():
    url = "http://127.0.0.1:5000/search"

    while True:
        query = input("Search for movies: ")

        data = {
            "query": query,
            "source": "imdb",
            "filter": {
                "type": "any",
                "amount": 10
            }
        }

        response = requests.get(url, json=data)

        with open(f"{query}.json", "w") as f:
            json.dump(response.json(), f, ensure_ascii=False)

        print(f"Writed search results to ./{query}.json\n")


if __name__ == '__main__':
    main()
