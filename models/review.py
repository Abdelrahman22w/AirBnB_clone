#!usr/bin/python3
"""Define the Review model subclass"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a sbclass of BaseModel class
    attribute:
        place_id: (str)
        user_id: (str)
        text: (str)
    """
    place_id = ""
    user_id = ""
    text = ""
