#!/usr/bin/env python3

import json
import time

import requests

from logger import logger


API = "https://rent.591.com.tw/home/search/rsList"
CONDITIONS = {
    'is_new_list': '1',
    'type': '1',
    'kind': '1',
    'searchtype': '1',
    'region': '1',
    'rentprice': '0,26000',
    'patternMore': '2',
    'option': 'cold',
    'hasimg': '1',
    'not_cover': '1',
}
WEB_URL_FORMAT_STR = "https://rent.591.com.tw/rent-detail-{}.html"

cache = set()


def get_houses():
    logger.info('requests 591 API...')
    response = requests.get(API, params=CONDITIONS)
    response_json = json.loads(response.text)

    try:
        data = response_json['data']
    except KeyError:
        logger.error("Cannnot get data from response_json")
    except:
        raise
    else:
        houses = data.get('data', [])
        logger.info(len(houses))

        for house in reversed(houses):
            yield house


def log_house_info(house):
    logger.info(
        "名稱：{}-{}-{}".format(
            house['region_name'],
            house['section_name'],
            house['fulladdress'],
        )
    )
    logger.info("網址：{}".format(WEB_URL_FORMAT_STR.format(house['post_id'])))
    logger.info("租金：{} {}".format(house['price'], house['unit']))
    logger.info("坪數：{} 坪".format(house['area']))
    logger.info("格局：{}".format(house['layout']))
    logger.info("更新時間：{}".format(time.ctime(house['refreshtime'])))
    logger.info("=" * 80)


def search_houses():
    houses = get_houses()
    for house in houses:
        if house['post_id'] in cache:
            break

        log_house_info(house)
        cache.update([house['post_id']])


def main():
    while True:
        search_houses()
        time.sleep(60)


if __name__ == "__main__":
    main()
