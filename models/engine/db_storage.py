#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages the storage with mysql."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine and session Mysql."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of models currently in storage."""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review
        objs = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
            return objs
        else:
            for obj in self.__session.query(User, State, City, Place).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
            return objs

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and Session."""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,expire_on_commit=False)
        self.__session = scoped_session(session_factory)
