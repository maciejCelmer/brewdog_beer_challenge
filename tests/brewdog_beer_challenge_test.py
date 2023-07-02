import pytest
import helpers.endpoints_helper as endpoints_helper
import helpers.validations_helper as validations_helper
from constants.variables import *


@pytest.fixture(scope='module')
def beers():
    params = {"brewed_after": BREWED_AFTER}
    beers_response = endpoints_helper.get_beers(params)
    assert beers_response.status_code == 200
    yield beers_response


def test_valid_beer_abv(beers):
    for beer in beers.json():
        validations_helper.check_if_beer_abv_is_valid(beer)


def test_valid_beer_name(beers):
    for beer in beers.json():
        validations_helper.check_if_beer_name_is_valid(beer)


def test_valid_first_brewed_date(beers):
    for beer in beers.json():
        validations_helper.check_if_beer_first_brewed_date_is_valid(beer, BREWED_AFTER)


def test_valid_beer_volume(beers):
    for beer in beers.json():
        validations_helper.check_if_beer_volume_is_valid(beer)

