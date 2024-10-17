from fastapi import APIRouter, FastAPI

from api.routes import jobs

API_V1_PREFIX = "/api/v1"


class Router:
    @staticmethod
    def create_app() -> FastAPI:
        app = FastAPI()
        api_router = APIRouter(prefix=API_V1_PREFIX)
        api_router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
        app.include_router(api_router)
        return app
