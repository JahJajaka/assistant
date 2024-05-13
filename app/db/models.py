import bcrypt
from sqlalchemy import DateTime, Column, ForeignKey, Integer, String, Text, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if key in dir(self):
                exec(f"self.{key} = {value}")

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now())

# Model for User
class User(Base, BaseMixin):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


# Model for Persona
class Persona(Base):
    __tablename__ = 'personas'
    persona_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(Text, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    user = relationship("User", back_populates="personas")

# Model for Event
class Event(Base):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    persona_id = Column(Integer, ForeignKey('personas.persona_id'), nullable=False)
    occurred_at = Column(TIMESTAMP, nullable=False)
    is_finished = Column(Boolean, server_default='f', nullable=False)
    persona = relationship("Persona", back_populates="events")

# Model for Tag
class Tag(Base):
    __tablename__ = 'tags'
    tag_id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String(255), nullable=False)
    event_id = Column(Integer, ForeignKey('events.event_id'), nullable=False)
    persona_id = Column(Integer, ForeignKey('personas.persona_id'), nullable=False)
    event = relationship("Event", back_populates="tags")
    persona = relationship("Persona", back_populates="tags")

# Setting up relationships
User.personas = relationship("Persona", order_by=Persona.persona_id, back_populates="user")
Persona.events = relationship("Event", order_by=Event.event_id, back_populates="persona")
Persona.tags = relationship("Tag", order_by=Tag.tag_id, back_populates="persona")
Event.tags = relationship("Tag", order_by=Tag.tag_id, back_populates="event")