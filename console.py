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


def parse(line: str):
    """Splits lines considering spaces"""
    args = shlex.split(line)
    return args, len(args)


class HBNBCommand(cmd.Cmd):
    """define the command interpreter"""
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

    """HBnB commands"""
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
        """clear terminal"""
        os.system("clear")

    def default(self, line: str) -> None:
        print(f"command \"{line}\" not found")

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_list = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
