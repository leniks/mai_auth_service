from fastapi import FastAPI
from typing import Optional
from schemas.User_schema import User, RegisterUser, AuthUser

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "bro like ahhh service"}

@app.get("/get_by_id/{id}")
def get_by_id_path(id: int) -> User:
    pass

@app.get("/get_by_id_param")
def get_by_id_param(user_id: Optional[str] = None) -> User:
    pass

@app.post("/register/")
def register_user_handler(user: RegisterUser):
    pass
