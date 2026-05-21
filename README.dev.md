## Documentation

To have a live view of the documentation install `docs/requirements.txt` and from root folder run:

```bash
sphinx-autobuild docs/source docs/build/html
```

Then go to `localhost:8000`.

## Local testing

Run `docker compose up --wait` in the repo root dir to setup postgres and influx before running pytest.
