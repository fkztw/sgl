API_URL = "https://rent.591.com.tw/home/search/rsList"

HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}

CONDITIONS = {
    'is_new_list': '1',
    'type': '1',
    'kind': '1',
    'searchtype': '1',
    'regionid': '1',
    'rentprice': '0,26000',
    'patternMore': '2',
    'option': 'cold',
    'hasimg': '1',
    'not_cover': '1',
}

WEB_URL_FORMAT_STR = "https://rent.591.com.tw/rent-detail-{}.html"

SETTINGS_PATH = "./settings.ini"
