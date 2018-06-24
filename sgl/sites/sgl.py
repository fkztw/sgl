from decimal import Decimal

import time

import requests
from bs4 import BeautifulSoup
from flask import current_app


ROOT_URL = "https://rent.591.com.tw"
API_URL = ROOT_URL + "/home/search/rsList"
WEB_URL_FORMAT_STR = ROOT_URL + "/rent-detail-{}.html"
MAP_URL_FORMAT_STR = ROOT_URL + "/map-houseRound.html?type=1&post_id={}&s=j_edit_maps&version=1"
HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}


def _reconstruct_payload(payload):
    # TODO
    new_payload = {
        'is_new_list': '1'
    }
    return new_payload


def _get_house_lat_and_lng(house):
    target = MAP_URL_FORMAT_STR.format(house['post_id'])
    response = requests.get(target, headers=HEADERS)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    lat = soup.find(id="lat").get('value')
    lng = soup.find(id="lng").get('value')

    return Decimal(lat), Decimal(lng)


def _reconstruct_houses(houses):
    new_houses = []
    for house in houses:
        new_house = {}

        new_house['name'] = "{}-{}-{}".format(
            house['region_name'],
            house['section_name'],
            house['fulladdress'],
        )

        new_house['url'] = "{}".format(WEB_URL_FORMAT_STR.format(house['post_id']))

        new_house['price'] = "{} {}".format(house['price'], house['unit'])

        new_house['area'] = "{} 坪".format(house['area'])

        new_house['layout'] = "{}".format(house['layout'])

        new_house['kind'] = "{}".format(house['kind_name'])

        new_house['update_time'] = "{}".format(time.ctime(house['refreshtime']))

        lat, lng = _get_house_lat_and_lng(house)
        new_house['lat'] = lat
        new_house['lng'] = lng

        new_houses.append(new_house)

    return new_houses


def get(payload):
    payload = _reconstruct_payload(payload)
    response = requests.get(API_URL, params=payload, headers=HEADERS)

    try:
        data = response.json()['data']
    except KeyError:
        current_app.logger.debug("response.json()['data']: {}".format(response.json()['data']))
        current_app.logger.error("Cannnot get data from response.json['data']")
    except Exception:
        current_app.logger.debug("response: {}".format(response.text))
        raise
    else:
        houses = data.get('data', [])
        houses = _reconstruct_houses(houses)
        return houses
