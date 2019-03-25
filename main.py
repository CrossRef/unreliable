from fastapi import FastAPI, HTTPException
import random
import time

HTTP_ERRORS = [404,408,500]

app = FastAPI()


@app.get("/")
def read_root():
    return 'Crossref unreliable server'

@app.get("/heartbeat")
def heartbeat():
    return {"status":"OK"}

@app.get("/error")
def random_error():
    e = random.choice(HTTP_ERRORS)
    raise HTTPException(status_code=e, detail="A random error")


@app.get("/timeout")
def timeout():
    time.sleep(35)
    return 'Crossref unreliable server will timeout alot'
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
