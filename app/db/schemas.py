from pydantic import BaseModel
from datetime import datetime

# Schema for User
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Schema for Persona
class PersonaBase(BaseModel):
    user_id: int
    description: str

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    persona_id: int
    updated_at: datetime

    class Config:
        from_attributes = True

# Schema for Event
class EventBase(BaseModel):
    description: str
    occurred_at: datetime
    is_finished: bool

class EventCreate(EventBase):
    persona_id: int 

class Event(EventBase):
    event_id: int
    persona_id: int  

    class Config:
        from_attributes = True

# Schema for Tag
class TagBase(BaseModel):
    tag_name: str
    event_id: int
    persona_id: int

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int

    class Config:
        from_attributes = True