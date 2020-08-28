#!/usr/bin/env python3

from decimal import Decimal
import concurrent.futures
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
    new_payload = {}

    if payload.get('is_new_list'):
        new_payload['is_new_list'] = ','.join(payload['is_new_list'])

    if payload.get('regionid'):
        new_payload['regionid'] = ','.join(payload['regionid'])

    if payload.get('rentprice_min') and payload.get('rentprice_max'):
        new_payload['rentprice'] = ','.join(payload['rentprice_min'] + payload['rentprice_max'])

    if payload.get('area_min') and payload.get('area_max'):
        new_payload['area'] = ','.join(payload['area_min'] + payload['area_max'])

    if payload.get('patternMore'):
        new_payload['patternMore'] = ','.join(payload['patternMore'])

    if payload.get('hasimg'):
        new_payload['hasimg'] = ','.join(payload['hasimg'])

    if payload.get('not_cover'):
        new_payload['not_cover'] = ','.join(payload['not_cover'])

    if payload.get('role'):
        new_payload['role'] = ','.join(payload['role'])

    if payload.get('option'):
        new_payload['option'] = ','.join(payload['option'])

    if payload.get('other'):
        new_payload['other'] = ','.join(payload['other'])

    return new_payload


def _get_processed_house_lat_and_lng(house):
    response = requests.get(
        MAP_URL_FORMAT_STR.format(house['post_id']),
        headers=HEADERS,
    )
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    lat = soup.find(id="lat").get('value')
    lng = soup.find(id="lng").get('value')

    return Decimal(lat), Decimal(lng)


def _get_processed_house_images_urls(house):
    response = requests.get(
        WEB_URL_FORMAT_STR.format(house['post_id']),
        headers=HEADERS,
    )
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    images_urls = [
        image.get("src").replace("125x85.crop", "765x517")
        for image in soup.find("div", {"class": "thumbnails"}).find_all("img")
    ]

    return images_urls


def _reconstruct_house(house):
    '''
    house = {
        'name': <str>,
        'url': <str>,
        'price': <str>,
        'area': <str>,
        'kind': <str>,
        'update_time': <datetime>,
        'images': [
            <str>,
            <str>,
            ...
        ],
        'lat': <decimal>,
        'lng': <decimal>,
    }
    '''

    # TODO: Save house images urls
    processed_house = {}

    processed_house['name'] = "{}-{}-{}".format(
        house['region_name'],
        house['section_name'],
        house['fulladdress'],
    )

    processed_house['url'] = "{}".format(WEB_URL_FORMAT_STR.format(house['post_id']))

    processed_house['price'] = "{} {}".format(house['price'], house['unit'])

    processed_house['area'] = "{} 坪".format(house['area'])

    processed_house['layout'] = "{}".format(house['layout'])

    processed_house['kind'] = "{}".format(house['kind_name'])

    processed_house['update_time'] = "{}".format(time.ctime(house['refreshtime']))

    # lat and lng, images have to be grabed from webpage,
    # they didn't show on the data queried from API.
    lat, lng = _get_processed_house_lat_and_lng(house)
    processed_house['lat'] = lat
    processed_house['lng'] = lng

    images_urls = _get_processed_house_images_urls(house)
    processed_house['images_urls'] = images_urls

    return processed_house


def _reconstruct_houses(houses):
    current_app.logger.info(f"total houses: {len(houses)}")

    start = time.time()
    processed_houses = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(houses)) as executor:
        futures = [executor.submit(_reconstruct_house, house) for house in houses]
        for future in concurrent.futures.as_completed(futures):
            try:
                processed_house = future.result()
            except Exception as e:
                current_app.logger.exeception(e)
            else:
                processed_houses.append(processed_house)
    end = time.time()
    current_app.logger.info(f"_reconstruct_houses() spent: {end - start} seconds")

    return processed_houses


def _set_csrf_token(session):
    r = session.get(ROOT_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.select('meta'):
        if tag.get('name', None) == 'csrf-token':
            csrf_token = tag.get('content')
            session.headers = HEADERS
            session.headers['X-CSRF-TOKEN'] = csrf_token
    else:
        print('No csrf-token found')


def get_houses(payload):
    payload = _reconstruct_payload(payload)
    current_app.logger.info("payload: {}".format(payload))
    session = requests.Session()
    _set_csrf_token(session)
    response = session.get(API_URL, params=payload, headers=HEADERS)

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
