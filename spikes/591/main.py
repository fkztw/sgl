#!/usr/bin/env python3

import time

import requests

from logger import logger
from constants import API_URL, CONDITIONS, WEB_URL_FORMAT_STR, HEADERS, \
    PARSE_INTERVAL_IN_SECONDS


cache = set()


def get_houses():
    logger.info('requests 591 API...')
    response = requests.get(API_URL, params=CONDITIONS, headers=HEADERS)

    try:
        data = response.json()['data']
    except KeyError:
        logger.debug("response.json()['data']: {}".format(response.json()['data']))
        logger.error("Cannnot get data from response.json['data']")
    except Exception:
        logger.debug("response: {}".format(response.text))
        raise
    else:
        houses = data.get('data', [])
        logger.info(len(houses))

        for house in houses:
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
    logger.info("\n")


def search_houses():
    houses = get_houses()
    for house in houses:
        if house['post_id'] in cache:
            continue

        log_house_info(house)
        cache.update([house['post_id']])


def main():
    while True:
        search_houses()
        time.sleep(PARSE_INTERVAL_IN_SECONDS)


if __name__ == "__main__":
    main()
