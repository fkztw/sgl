# sgl

A simple crawler for <https://rent.591.com.tw/>

- Pure CLI version already moved to [`scripts/591`](./scripts/591)
- Now mainly focus on web version
    - A Flask website on localhost
    - Show places on Google Maps
        - **Google Maps API key NEEDED!!**

---

## Development

- **Require** `poetry`: `pip install poetry`
- `make install`

### CLI version

- `make run-cli`

### Web version

- [You need to get a Google Maps API key for using it](https://developers.google.com/maps/documentation/javascript/get-api-key)
- `env GOOGLEMAPS_KEY="xxxx" make run-server`
    - Change xxxx to the API key you got
