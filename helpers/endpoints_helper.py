import requests
from constants.endpoints import *


def get_page_beers(params=None):
    response = requests.get(BASE_URL+GET_BEERS_ENDPOINT, params=params)
    assert response.status_code == 200
    return response


def get_beers(params=None):
    page_no = 1
    params["page"] = page_no
    beers_response = get_page_beers(params)
    beers = beers_response.json()

    last_page = False

    while len(beers) % 25 == 0 and not last_page:
        page_no = page_no + 1
        params["page"] = page_no
        next_page_beers_response = get_page_beers(params)
        if len(next_page_beers_response.json()) < 25:
            last_page = True
        beers.extend(next_page_beers_response.json())

    return beers
