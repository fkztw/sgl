# sgl

A simple crawler for <https://www.591.com.tw/>

- Pure CLI version already moved to [`scripts/591`](./scripts/591)
- Now mainly focus on web version
    - A Flask website on localhost
    - Show places on Google Map
        - Need Google Map API key

---

## Development

- **Require** `pipenv`: `pip install pipenv`
- `make install`
- `env GOOGLEMAPS_KEY=xxxx make run-server`


### Google Maps API key

[You need to get a Google Maps API key for using it](https://developers.google.com/maps/documentation/javascript/get-api-key)
