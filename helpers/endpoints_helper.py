import requests
from constants.endpoints import *


def get_beers(params=None):
    response = requests.get(BASE_URL+GET_BEERS_ENDPOINT, params=params)
    return response
