from fastapi import FastAPI

from app.apis import timedifference

app = FastAPI()

app.include_router(
    timedifference.router,
    prefix="/timedifference",
    tags=["TimeDifference"],
)
