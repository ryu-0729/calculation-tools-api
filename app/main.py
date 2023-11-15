from fastapi import FastAPI

from app.apis import overtime

app = FastAPI()

app.include_router(overtime.router, prefix="/overtime", tags=["OverTime"])
