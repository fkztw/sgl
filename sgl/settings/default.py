import os

# Flask-GoogleMaps settings
GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY')

# Flask-WTF settings
WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or os.urandom(32)

# Flask settings
SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)

# sgl settings
PAGE_TITLE = os.environ.get('PAGE_TITLE') or "sgl"
