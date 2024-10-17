from fastapi import FastAPI
from api.routes import router
from container import AppContainer


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


# TODO: Sort out persistence
def create_db():
    pass


# Wire up dependency injection.
container = AppContainer()

# Spin up the API server.
app = create_app()
