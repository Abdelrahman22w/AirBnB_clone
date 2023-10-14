#!/usr/bin/python3
"""Define the HBnB console"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
import shlex
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

    def do_create(self, args):
        """
        Create a new instance of a class and print its ID.
        Args:
        args (str): The user's input containing the class name.
        """
        arg_list = parse(args)

        if not arg_list:
            print("** class name missing **")

        class_name = arg_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        if len(arg_list) > 1:
            print("** Too many arguments for create **")

        new_instance = eval(class_name)()

        print(new_instance.id)

        storage.save()

    def do_show(self, args):
        """
        Show the string representation of an instance
        based on the class name and id.

        Args:
        args (str): The user's input containing the class name and instance ID.
        """
        arg_list = parse(args)

        object_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")

        class_name = arg_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        if len(arg_list) == 1:
            print("** instance id missing **")

        instance_key = "{}.{}".format(class_name, arg_list[1])

        if instance_key not in object_dict:
            print("** no instance found **")

        print(object_dict[instance_key])

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id.

        Args:
        args (str): The user's input containing the class name and instance ID.
        """
        arg_list = parse(args)

        object_dict = storage.all()

        if len(arg_list) < 2:
            print("** arguments missing **")

        class_name, instance_id = arg_list[0], arg_list[1]

        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key in object_dict:
            del object_dict[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Print string representations of instances based on optional class name
        Args:
        args (str): The user's input containing the optional class name.
        """
        arg_list = parse(args)
        object_dict = storage.all()

        class_name = arg_list[0] if arg_list else None
        obj_list = [str(obj) for obj in object_dict.values()
                    if not class_name or obj.__class__.__name__ == class_name]

        if not obj_list:
            print("** no instances found **")
        else:
            print(obj_list)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
    <class>.update(<id>, <attribute_name>, <attribute_value>) or
    <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        arg_list = parse(arg)
        obj_dict = storage.all()

        if len(arg_list) < 4:
            print("** Missing arguments **")
            return False

        class_name, instance_id, attribute_name, attribute_value = arg_list[0], arg_list[1], arg_list[2], arg_list[3]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key not in obj_dict.keys():
            print("** no instance found **")
            return False

        obj = obj_dict[instance_key]

        if attribute_name not in obj.__class__.__dict__.keys():
            print("** attribute name doesn't exist **")
            return False

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, or updated_at **")
            return False

        attr_type = type(obj.__class__.__dict__[attribute_name])

        try:
            attribute_value = attr_type(attribute_value)
        except ValueError:
            print("** invalid attribute value **")
            return False

        obj.__dict__[attribute_name] = attribute_value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
