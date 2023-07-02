def get_beer_info(beer):
    beer_id = beer["id"]
    beer_name = beer["name"]
    return "beer_id: {}; beer_name: {}; ".format(beer_id, beer_name)
