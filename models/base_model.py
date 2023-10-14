#!/usr/bin/python3
"""Define the basemodle class for the project."""
import models
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Define the BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any type): unused
            **kwargs (dict): the key and value of the attributes
        """
        dateFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or j == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, dateFormat)
                else:
                    self.__dict__[i] = j
        else:
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
