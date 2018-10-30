import requests
from bs4 import BeautifulSoup


ROOT_URL = "https://rent.591.com.tw"
WEB_URL_FORMAT_STR = ROOT_URL + "/rent-detail-{}.html"
MAP_URL_FORMAT_STR = ROOT_URL + "/map-houseRound.html?type=1&post_id={}&s=j_edit_maps&version=1"
POST_ID = 6471153
HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}

target = MAP_URL_FORMAT_STR.format(POST_ID)
print(target)
res = requests.get(target, headers=HEADERS)
html = res.content
soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="lng").get('value'))
