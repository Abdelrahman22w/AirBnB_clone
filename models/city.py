#!usr/bin/python3
"""Define the city model subclass"""

from models.base_model import BaseModel


class City(BaseModel):
    """a sbclass of BaseModel class
    attribute:
        state_id: (str)
        name: (str)
    """
    state_id = ""
    name = ""
