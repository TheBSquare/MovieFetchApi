
import requests


def main():
    url = "http://127.0.0.1:5000/search"

    data = {
        "query": "мавка",
        "source": "imdb",
        "filter": {
            "type": "any",
            "amount": 5
        }
    }

    response = requests.get(url, json=data)
    print(response.json()["description"])


if __name__ == '__main__':
    main()
