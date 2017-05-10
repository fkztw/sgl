#!/usr/bin/env python3

import re
import time

import requests
import bs4

from logger import logger


url = 'https://rent.591.com.tw/new/?kind=1&region=1&rentprice=0,26000&patternMore=2&option=cold&hasimg=1&not_cover=1&order=posttime&orderType=desc'
link_pattern = re.compile('//rent.591.com.*')
cache = set()


def get_links():
    logger.info('requests 591 ...')
    response = requests.get(url)
    html = bs4.BeautifulSoup(response.text, 'html.parser')
    houses = filter(lambda x: x and x != '\n', html.find(id='content').children)
    houses = map(lambda x: x.find(href=link_pattern), houses)
    houses = map(lambda x: 'https:' + x.get('href').strip(), houses)
    return tuple(houses)


def search_houses():
    houses = get_links()
    for h in houses:
        if h in cache:
            break
        logger.info('new house: {}'.format(h))
    cache.update(houses)


def main():
    while True:
        search_houses()
        time.sleep(10)


if __name__ == "__main__":
    main()
