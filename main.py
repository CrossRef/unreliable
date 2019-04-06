import random
import time
from os import getpid
from fastapi import FastAPI, HTTPException
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    Counter,
    Gauge,
    Summary,
    generate_latest,
    multiprocess,
)
from pydantic import BaseModel
from starlette.responses import Response
from starlette_prometheus import PrometheusMiddleware, metrics


class Heartbeat(BaseModel):
    status: str
    pid: int


HTTP_ERRORS = [404, 408, 500, 503]


app = FastAPI()
app.add_middleware(PrometheusMiddleware)


@app.get("/")
def read_root():
    return "Crossref unreliable server pid: {}".format(getpid())


@app.get("/heartbeat", response_model=Heartbeat)
def heartbeat():
    return Heartbeat(status="OK", pid=getpid())


@app.get("/error")
def random_error():
    e = random.choice(HTTP_ERRORS)
    raise HTTPException(status_code=e, detail="A random error")


@app.get("/timeout")
def timeout():
    time.sleep(random.randint(0, 35))
    return "Crossref unreliable server will timeout alot"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, media_type=CONTENT_TYPE_LATEST)
