from fastapi import FastAPI
from paths.items import RouterItem
from configuration.database import engine, meta

app = FastAPI()

app.include_router(RouterItem)

meta.create_all(engine)
