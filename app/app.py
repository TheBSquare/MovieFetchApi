
import requests

from flask import Flask, request, jsonify
from flask_expects_json import expects_json
from flask_cors import CORS

from .scheme import SEARCH_SCHEMA, DETAILS_SCHEMA, STREAM_SCHEMA
from dtypes.response import OkResponse, ErrResponse
from dtypes.search import to_search
from dtypes.source import to_source


app = Flask(__name__)
cors = CORS(app, resources={r"/master/*": {"origins": "*"}})


@app.route("/search")
@expects_json(SEARCH_SCHEMA)
def handle_search():
    data = request.json

    filters = data.get("filter") if data.get("filter") else {}
    query = data["query"]
    if not len(query):
        return ErrResponse("Query is empty").to_json()

    source = to_source(data["source"])
    if not source:
        return ErrResponse("Cant find such source").to_json()

    search = to_search(source)
    if not search:
        return ErrResponse(f"Cant find search engine").to_json()

    search.apply(query, filters)
    response = search.search()
    if response.is_err():
        return response.to_json()

    response = search.filter()
    return response.to_json()


@app.route("/details")
@expects_json(DETAILS_SCHEMA)
def handle_details():
    pass


@app.route("/stream")
@expects_json(STREAM_SCHEMA)
def handle_stream():
    pass


if __name__ == '__main__':
    app.run()
