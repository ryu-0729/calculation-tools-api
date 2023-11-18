from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.apis import timedifference

app = FastAPI()

app.include_router(
    timedifference.router,
    prefix="/timedifference",
    tags=["TimeDifference"],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Calculation Tools API",
        version="1.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
