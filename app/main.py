from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate

from app import config
from app.routes import users
from app.db import database
from app.db.models import User, Persona, Event, Tag, Base
from app.db.schemas import UserCreate, User as PyUser, PersonaCreate, Persona as PyPersona, EventCreate, \
    Event as PyEvent, TagCreate, Tag as PyTag

from sqlalchemy.orm import Session

from app.llm.llm import get_model

Base.metadata.create_all(bind=database.engine)
app = FastAPI(debug=config.IS_DEBUG)
app.include_router(users.router)

def get_db():
    db_ = database.SessionLocal()
    try:
        yield db_
    finally:
        db_.close()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/", response_model=PyUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=PyUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/personas/", response_model=PyPersona)
def create_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    db_persona = Persona(**persona.dict())
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

@app.get("/personas/{persona_id}", response_model=PyPersona)
def read_persona(persona_id: int, db: Session = Depends(get_db)):
    db_persona = db.query(Persona).filter(Persona.persona_id == persona_id).first()
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return db_persona

@app.post("/events/", response_model=PyEvent)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.get("/events/{event_id}", response_model=PyEvent)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@app.post("/tags/", response_model=PyTag)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

@app.get("/tags/{tag_id}", response_model=PyTag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.query(Tag).filter(Tag.tag_id == tag_id).first()
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


class LlmRequest(BaseModel):
    prompt: str

@app.post("/llm")
def llm(request: LlmRequest):
    prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
    chain = prompt | get_model()
    result = chain.invoke({"topic": request.prompt})
    return {"message": result}
