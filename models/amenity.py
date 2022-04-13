#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('', Base.metadata,
                          Column('', ForeignKey('left.id')),
                          Column('right_id', ForeignKey('right.id')))


class Amenity(BaseModel, Base):
    """Class Representing amenities."""

    from models.place import place_amenity
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenties = relationship("Place", secondary=place_amenity)
