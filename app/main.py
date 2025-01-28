from fastapi import FastAPI
import os
from typing import Optional

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "router service"}


@app.post("auth/login")
def login():
    pass
