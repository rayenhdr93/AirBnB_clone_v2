#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """Represent State Model."""

    from models import storage_t

    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)
