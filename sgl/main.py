#!/usr/bin/env python3

import re
import time

import requests
import bs4

from logger import logger


url = 'https://rent.591.com.tw/new/?kind=1&region=1&rentprice=0,26000&patternMore=2&option=cold&hasimg=1&not_cover=1'
link_pattern = re.compile('//rent.591.com.*')
cache = set()


def content_clean_up(string):
    return ''.join(map(str.strip, string.split()))


def get_houses():
    logger.info('requests 591 ...')
    response = requests.get(url)
    html = bs4.BeautifulSoup(response.text, 'html.parser')
    houses = tuple(
        filter(
            lambda x: x and x != '\n',
            html.find(id='content').children
        )
    )
    links = map(lambda x: x.find(href=link_pattern), houses)
    links = map(lambda x: 'https:' + x.get('href').strip(), links)
    descriptions = map(
        lambda x: ''.join(
            map(
                lambda s: content_clean_up(s.text),
                x.find_all(class_="lightBox")
            )
        ),
        houses
    )
    return tuple(zip(links, descriptions))


def search_houses():
    houses = get_houses()
    for h in houses:
        if h in cache:
            break
        logger.info('new house: {}'.format(h))
    cache.update(houses)


def main():
    while True:
        search_houses()
        time.sleep(60)


if __name__ == "__main__":
    main()
