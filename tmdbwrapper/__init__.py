import os
import requests

TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. "
        "See https://v.gd/tmdb_api_introduction for "
        "information how to set up such an API key."
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY

from .tv import TV
