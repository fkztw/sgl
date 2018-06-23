from flask import Blueprint, render_template, current_app, request
from flask_googlemaps import Map


BP = Blueprint('root', __name__)


@BP.route("/", methods=["GET"])
def index():
    return render_template(
        'index.html',
        title=current_app.config.get('INDEX_PAGE_TITLE'),
    )

@BP.route("/map", methods=["GET"])
def map():
    # TODO
    # payload = request.json or request.form
    # Get rental locations

    # TODO
    # Add all locations's lat and lng into markers
    # markers =

    google_map = Map(
        identifier='sgl_map',
        lat=25.044955,
        lng=121.335579,
        style='height:80%;width:80%;margin:1%;',
        language='zh-tw',
        region='TW',
    )

    return render_template(
        'map.html',
        title=current_app.config.get('MAP_PAGE_TITLE'),
        google_map=google_map,
    )
