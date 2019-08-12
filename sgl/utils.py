from decimal import Decimal


def _build_infobox(house):
    infobox = ""
    infobox += "<h2><a target='_blank' href={url}>{name}</a></h2><br/>\n".format(
        name=house['name'],
        url=house['url'],
    )
    infobox += "<img src='{}'><br/><br/>\n".format(house['cover_image_url'])
    infobox += "租金：{}<br/>\n".format(house['price'])
    infobox += "坪數：{}<br/>\n".format(house['area'])
    infobox += "更新時間：{}<br/>\n".format(house['update_time'])

    return infobox


def get_markers(houses):
    markers = []
    for house in houses:
        marker = {}
        marker['title'] = house['name']
        marker['lat'] = house['lat']
        marker['lng'] = house['lng']
        marker['infobox'] = _build_infobox(house)
        markers.append(marker)

    return markers


def get_center_spot(houses):
    lat_sum, lng_sum = Decimal(0), Decimal(0)
    valid_count = 0
    for house in houses:
        lat, lng = house['lat'], house['lng']

        # Reasonable location in Taiwan
        if 21 <= lat <= 26 and 119 <= lng <= 122:
            lat_sum += lat
            lng_sum += lng
            valid_count += 1

    if valid_count == 0:
        # Center of Taiwan
        return 23.97565, 120.97388

    lat_avg = lat_sum/valid_count
    lng_avg = lng_sum/valid_count

    return lat_avg, lng_avg
