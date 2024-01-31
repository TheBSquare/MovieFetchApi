# MovieFetch api
Babobab studio production

## Usage

### Installing python

    install python

### Installing requirements

    ./MovieFetch python3.v -m pip install -r requirements.txt

### Run app

    ./MovieFetch python3.v main.py

## Endpoints

### Search

#### Make search
    GET .../search
    request: {
        "query": "titanic",
        "source": "imdb",
        "filter": {
            "type": "any",
            "amount": 10
        }
    }
    response: {
        'data': [
            {
                'author': {
                    'birthday': {'timestamp': None}, 
                    'first_name': None, 
                    'surname': None
                }, 
                'movie_id': {
                    'movie_id': 'tt0120338', 
                    'source': 'imdb'
                }, 
                'movie_type': {
                    'original': 'movie', 
                    'simple': 'movie'
                }, 
                'poster': {
                    'height': 3000, 
                    'url': 'https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg', 
                    'width': 2015
                }, 
                'rank': {
                    'position': 335, 
                    'source': 'imdb'
                }, 'release': {'timestamp': 852069600}, 
                'subtitle': 'Leonardo DiCaprio, Kate Winslet', 
                'title': 'Titanic', 
                'trailer': [
                    {
                        'movie_id': {
                            'movie_id': 'vi1740686617', 
                            'source': 'imdb'
                        }, 
                        'poster': {
                            'height': 1080, 
                            'url': 'https://m.media-amazon.com/images/M/MV5BYzExZDkwNzYtYmI0Mi00OThhLWFhNmMtZTZjYWU2MTdkMDAzXkEyXkFqcGdeQWRpZWdtb25n._V1_.jpg', 
                            'width': 1920
                        }, 
                        'subtitle': '1:37', 
                        'title': 'Official Trailer'
                    },
                    ...
                ]
            },
            ...
        ]
    }

#### List search sources

    GET .../search/sources
    request: null
    response: {
        "data": ["imdb"], 
        "description": "ok", 
        "status": "ok"
    }
