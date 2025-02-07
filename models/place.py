#!/usr/bin/python3
"""Place Module for HBNB project."""
from os import getenv
from models.base_model import BaseModel, Base
from models import storage, storage_t
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

if storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """Define a Place model."""

    from models.city import City
    from models.user import User

    if storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey(City.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Get reviews for file storage."""
            return [review for review in storage.all('Review').values()
                    if self.id == review.place_id]

        @property
        def amenities(self):
            """Get amenities for file storage."""
            return self.__class__.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == "Amenity":
                self.__class__.amenity_ids.append(obj.id)
