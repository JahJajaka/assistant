from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db import SessionLocal
from app.db.models import User

router = APIRouter()


class UserPasswordRequest(BaseModel):
    username: str
    password: str


@router.post("/signup/")
async def signup(request: UserPasswordRequest):
    user = User(username=request.username)
    user.set_password(request.password)
    db = SessionLocal()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login/")
async def login(request: UserPasswordRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not user.check_password(request.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"message": "Login successful"}


@router.post("/logout/")
async def logout():
    # Logic for logging out
    return {"message": "Logout successful"}
