#!/usr/bin/python3
"""Define the basemodle class for the project."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Define the BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initializes class instances, attributes(uuid, created/updated)
        If kwargs is not empty its creates an instance
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    created = datetime.fromisoformat(value)
                    self.created_at = created
                elif key == 'updated_at':
                    updated = datetime.fromisoformat(value)
                    self.updated_at = updated
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """update the (updated_at) to current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

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
