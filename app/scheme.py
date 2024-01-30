
SEARCH_SCHEMA = {
    "type": "object",
    "properties": {
        "query": {"type": "string"},
        "source": {"type": "string"},
        "filter": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "amount": {"type": "number"}
            },
            "required": ["type", "amount"]
        },
    },
    "required": ["query", "filter"]
}

DETAILS_SCHEMA = {
    "type": "object",
    "properties": {
        "imdb_id": {"type": "string"},
        "source": {"type": "string"}
    },
    "required": ["imdb_id", "source"]
}

STREAM_SCHEMA = {
    "type": "object",
    "properties": {
        "url": {"type": "string"},
        "source": {"type": "string"}
    },
    "required": ["url", "source"]
}
