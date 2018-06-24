from decimal import Decimal


def get_markers(houses):
    pass


def get_center_spot(houses):
    lat_sum, lng_sum = Decimal(0), Decimal(0)
    for house in houses:
        lat_sum += house['lat']
        lng_sum += house['lng']

    return lat_sum/len(houses), lng_sum/len(houses)
