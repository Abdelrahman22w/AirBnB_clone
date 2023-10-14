#!/usr/bin/python3
"""Define the HBnB console"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
import shlex
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


import cmd
import os
from models import storage
from models.base_model import BaseModel

def parse(line: str):
    """Splits lines considering spaces and returns args and num_args"""
    args = line.split()
    num_args = len(args)
    return args, num_args

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, args):
        """Quit the command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit the command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_clear(self, args):
        """Clear the terminal"""
        os.system("clear")

    def default(self, line: str):
        """Handle unrecognized commands."""
        print(f"Command '{line}' not found")




if __name__ == "__main__":
    HBNBCommand().cmdloop()
