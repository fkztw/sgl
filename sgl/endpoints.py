from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
)
from flask_googlemaps import Map

from sgl.forms import QueryForm


BP = Blueprint('root', __name__)


@BP.route("/", methods=["GET"])
def index():
    form = QueryForm()

    return render_template(
        'index.html',
        title=current_app.config.get('INDEX_PAGE_TITLE'),
        form=form,
    )


@BP.route("/map", methods=["POST"])
def query_map():
    # TODO
    payload = request.json or request.form
    print(payload)
    # Get rental locations

    # TODO
    # Add all locations's lat and lng into markers
    markers = None

    # TODO
    # Get centered object lat and lng
    lat, lng = 25.04, 121.32

    google_map = Map(
        identifier='sgl_map',
        lat=lat,
        lng=lng,
        markers=markers,
        style='height:80%;width:80%;margin:1%;',
        language='zh-tw',
        region='TW',
    )

    return render_template(
        'map.html',
        title=current_app.config.get('MAP_PAGE_TITLE'),
        google_map=google_map,
    )
