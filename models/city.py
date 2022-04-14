#!/usr/bin/python3
"""City Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The city class, contains state ID and name."""

    from models import storage_t
    from models.state import State

    if storage_t == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)
