import os

# Flask-GoogleMaps settings
GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY')

# sgl settings
INDEX_PAGE_TITLE = os.environ.get('INDEX_PAGE_TITLE')
MAP_PAGE_TITLE = os.environ.get('MAP_PAGE_TITLE')
PARSE_INTERVAL_IN_SECONDS = os.environ.get('PARSE_INTERVAL_IN_SECONDS') or 1800
