## DTO/Domain/Data

This project is intended for learning:

* Python
* Dependency injection (`dependency-injector`)
* API framework (`FastAPI`)
* DTO models (`Pydantic`)
* Domain model (used within the application)
* Data models (`SQLAlchemy`)

If you stumbled upon this project, hopefully it's in a state where there's a clear separation of DTO/domain/data objects.

It's a work in progress...

## Requirements

* [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installing UV

Read the [getting started](https://docs.astral.sh/uv/getting-started/installation/) page for installation instructions.

If that's TL;DR then:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installing Python

Use `uv` to install Python `3.12.6`:

```
uv python install 3.12.6
```

## Setup instructions

1. Clone the repo

    ```
    git clone git@github.com:peteski22/dto-domain-data.git && \
    cd dto-domain-data
    ```

2. Create and activate the Python virtual environment

    ```
    uv venv -p=3.12 && \
    source .venv/bin/activate
    ```

3. Synchronise the dependencies within the project

    ```
    uv sync
    ```

4. Start up the HTTP web server (API)

    ```
    fastapi dev main.py
    ```