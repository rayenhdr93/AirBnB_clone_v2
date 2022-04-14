#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """Class Representing amenities."""

    if models.storage_t == 'db':
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenties = relationship("Place", secondary=place_amenity)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity."""
        super().__init__(*args, **kwargs)
