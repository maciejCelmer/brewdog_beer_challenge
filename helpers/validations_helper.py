from datetime import datetime
import helpers.beer_info_reader as beer_info_reader


def check_if_beer_abv_is_valid(beer):
    beer_abv = beer["abv"]

    assert type(beer_abv) is float, beer_info_reader.get_beer_info(beer)+"Beer abv must be a float, but is {}-{}".format(type(beer_abv), beer_abv)
    assert beer_abv is not None, beer_info_reader.get_beer_info(beer)+"Beer abv must not be a None"
    assert len(str(beer_abv)) != 0, beer_info_reader.get_beer_info(beer)+"Beer abv must not be an empty string"
    assert beer_abv > 4.0, beer_info_reader.get_beer_info(beer)+"Beer abv must be greater than 4.0"


def check_if_beer_name_is_valid(beer):
    beer_name = beer["name"]
    assert beer_name is not None, beer_info_reader.get_beer_info(beer)+"Beer name must not be a None"
    assert len(str(beer_name)) != 0, beer_info_reader.get_beer_info(beer)+"Beer name must not be an empty string"


def check_if_beer_first_brewed_date_is_valid(beer, beers_breded_after_date):
    beer_first_brewed_date = beer["first_brewed"]

    timestamp_beer_first_brewed_date = datetime.strptime(beer_first_brewed_date, "%m/%Y").timestamp()
    timestamp_beers_breded_before_date = datetime.strptime(beers_breded_after_date, "%m-%Y").timestamp()
    print(timestamp_beer_first_brewed_date)
    print(timestamp_beers_breded_before_date)

    assert timestamp_beer_first_brewed_date >= timestamp_beers_breded_before_date, beer_info_reader.get_beer_info(beer)+"Beer first brewed timestamp is lower than requested from API"


def check_if_beer_volume_is_valid(beer):
    beer_volume = beer["volume"]

    assert type(beer_volume) is dict, beer_info_reader.get_beer_info(beer)+"Beer volume must be a dictionary"
    assert "value" in beer_volume, beer_info_reader.get_beer_info(beer)+"Beer volume must contains value key"
    assert "unit" in beer_volume, beer_info_reader.get_beer_info(beer)+"Beer volume must contains unit key"
