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
</div>
'''.format(
    house['url'],
    house['name'],
    house['price'],
    house['area'],
    house['update_time'],
)

    # Use Boostrap Carousel for house images preview
    infobox += '''
  <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
'''
    for i, image_url in enumerate(house['images_urls']):
        if i == 0:
            infobox += '''
      <div class="carousel-item active">
        <img src="{}" class="d-block w-100">
      </div>
'''.format(image_url)

        else:
            infobox += '''
      <div class="carousel-item">
        <img src="{}" class="d-block w-100">
      </div>
'''.format(image_url)
    else:
        infobox += "    </div>"

    infobox +='''
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon bg-dark" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon bg-dark" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
'''

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
