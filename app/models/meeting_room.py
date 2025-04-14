# app/models/meeting_room.py

# Импортируем из Алхимии нужные классы.
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

# Импортируем базовый класс для моделей.
from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    reservations = relationship('Reservation', cascade='delete')
