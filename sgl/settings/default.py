import os

# Flask-GoogleMaps settings
GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY')

# Flask-WTF settings
WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')

# Flask settings
SECRET_KEY = os.environ.get('SECRET_KEY')

# sgl settings
INDEX_PAGE_TITLE = os.environ.get('INDEX_PAGE_TITLE')
MAP_PAGE_TITLE = os.environ.get('MAP_PAGE_TITLE')
