#!/usr/bin/python3
"""Define the basemodle class for the project."""

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Define the BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """update the (updated_at) to current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Return the dictionary of instance of the BaseModel"""
        temp = self.__dict__.copy()
        temp["__class__"] = type(self).__name__
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        return temp

    def __str__(self):
        """Return the string representation of the Basemodel instance"""
        class_name = self.__class__.__name__
        return ("[{}] ({})   {}".
                format(class_name, self.id, self.__dict__))
