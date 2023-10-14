#!usr/bin/python3

"""Define the FileStorage class"""

import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """Storage engine for the AirBnB clone project."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return a dictionary of objects."""
        # Access __objects using the class name
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary."""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            # Access __objects using the class name
            FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file."""
        ser_objects = {key: obj.to_dict()
                       for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(ser_objects, file)

    def reload(self):
        """Deserialize objects from a JSON file."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as file:
                ser_objects = json.load(file)
                for key, obj_dict in ser_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals().get(class_name)
                    if obj_class:
                        obj = obj_class(**obj_dict)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
