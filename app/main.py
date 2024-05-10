from fastapi import FastAPI
from app import config
from app.routes import users

app = FastAPI(debug=config.IS_DEBUG)
app.include_router(users.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
