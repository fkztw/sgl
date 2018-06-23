import os

# Flask-GoogleMaps settings
GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY')

# sgl settings
PARSE_INTERVAL_IN_SECONDS = os.environ.get('PARSE_INTERVAL_IN_SECONDS') or 1800
