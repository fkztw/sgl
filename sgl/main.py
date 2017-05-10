#!/usr/bin/env python3

import json
import time

import requests

from logger import logger
from constants import API_URL, CONDITIONS, WEB_URL_FORMAT_STR, SETTINGS_PATH


cache = set()


def get_houses():
    logger.info('requests 591 API...')
    response = requests.get(API_URL, params=CONDITIONS)
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
