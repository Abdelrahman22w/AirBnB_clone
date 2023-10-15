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
    """Splits lines considering spaces and returns args and num_args"""
    args = line.split()
    num_args = len(args)
    return args, num_args


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
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

    def do_create(self, line):
        """Create a new object"""
        class_name = line.strip()

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.__class__.__classes:
            print("** class doesn't exist **")
        else:
            new_object = self.__class__.__classes[class_name]()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args, num_args = parse(line)
        if num_args == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__.__classes:
            print("** class doesn't exist **")
        elif num_args < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = class_name + "." + obj_id
            all_instances = storage.all()
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print string representation of all instances"""
        obj_list = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)
        print(obj_list)

    def do_destroy(self, line):
        """Destroys an instance based on the class name and id"""
        args, num_args = parse(line)
        all_instances = storage.all()

        if num_args == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__class__.__classes:
            print("** class doesn't exist **")
            return
        if num_args < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in all_instances:
            print("** no instance found **")
            return

        del all_instances[key]
        storage.save()

    def do_update(self, line):
        """Updates attributes of an object"""
        updates = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif updates[0] not in __class__.__classes:
            print("** class doesn't exist **")
            return
        elif len(updates) == 1:
            print("** instance id missing **")
            return
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + updates[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
