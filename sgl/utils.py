from decimal import Decimal


def _build_infobox(house):
    infobox = '''
<div class="card">
  <div class="card-body">
    <h5 class="card-title"><a target="_blank" href="{}">{}</a></h5>
    <p class="card-text">
      <h6>租金：{}</h6>
      <h6>坪數：{}</h6>
      <h6>更新時間：{}</h6>
    </p>
  <div>
  <img src="{}" class="card-img-bottom">
</div>
'''.format(
    house['url'],
    house['name'],
    house['price'],
    house['area'],
    house['update_time'],
    house['cover_image_url'],
)

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
