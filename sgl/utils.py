from decimal import Decimal


def _build_infobox(house):
    infobox = ""
    infobox += "<h2><a href={url}>{name}</a></h2><br/>\n".format(
        name=house['name'],
        url=house['url'],
    )
    infobox += "租金：{}<br/>\n".format(house['price'])
    infobox += "坪數：{}<br/>\n".format(house['area'])

    return infobox

def get_markers(houses):
    markers = []
    for house in houses:
        marker = {}
        marker['lat'] = house['lat']
        marker['lng'] = house['lng']
        marker['infobox'] = _build_infobox(house)
        markers.append(marker)

    return markers

def get_center_spot(houses):
    lat_sum, lng_sum = Decimal(0), Decimal(0)
    for house in houses:
        lat_sum += house['lat']
        lng_sum += house['lng']

    return lat_sum/len(houses), lng_sum/len(houses)
