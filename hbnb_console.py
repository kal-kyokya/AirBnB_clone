#!/usr/bin/python3
"""
'console' is the entry point to the AirBnB console
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Collection of attributes and methods enabling command interpretation.

    Parent Class:
        Cmd: Provides class fields for command manipulation.
    """

    prompt = "(hbnb) "
    cls_list = ["BaseModel", "User", "Amenity",
                "Place", "State", "City", "Review"]

    def do_quit(self, line):
        """Executes for input command 'quit'.

        Arg:
            line: Potential input parameter to the 'quit' command.

        Usage:
            (hbnb) quit
        """
        return (True)

    def help_quit(self):
        """Documentation for help input command linked to auit command."""
        print("When called, will exit/terminate the program.")

    def do_EOF(self, line):
        """Executes to exit cmdloop().

        Arg:
            line: Potential input parameter to the 'quit' command.

        Usage:
            (hbnb) ^D
        """
        print()
        return (True)

    def help_EOF(self):
        """Documentation for End Of File signals as input (i.e. CTRL-D)"""
        print("Handles 'CTRL-D' as input command and terminates execution.")

    def emptyline(self):
        """Executes when input command is 'an empty string'."""
        pass

    def do_create(self, cls_type=None):
        """Initializes an object of specific class type.

        Arg:
            cls_type: Input string containing
                      the desired class type for object to be constructed.

        Usage:
            (hbnb) create <class name>
        """
        parsing_result = cmd.Cmd.parseline(self, cls_type)
        if parsing_result[0] is None:
            print("** class name missing **")
        elif parsing_result[0] not in self.cls_list:
            print("** class doesn't exist **")
        else:
            obj = eval(cls_type)()
            storage.new(obj)
            storage.save()
            print(f"{obj.id}")

    def help_create(self):
        """Documentation for the 'create' interpreter command."""
        print("Constructs/Initializes an object of defined class type.")

    def do_show(self, cls_and_id):
        """Prints an instance's infos based on its class name and unique ID.

        Arg:
            cls_and_id: String contained sought object's class and ID.

        Usage:
            (hbnb) show <class name> <id>
        """
        parsing_result = cmd.Cmd.parseline(self, cls_and_id)
        if parsing_result[0] is None:
            print("** class name missing **")
        elif parsing_result[0] not in self.cls_list:
            print("** class doesn't exist **")
        elif parsing_result[1] == "":
            print("** instance id missing **")

        else:
            my_dict = storage.all()
            if f"{parsing_result[0]}.{parsing_result[1]}" in my_dict:
                print(my_dict[f"{parsing_result[0]}.{parsing_result[1]}"])
            else:
                print("** no instance found **")

    def help_show(self):
        """Documentation for the 'show' command as interpreter input."""
        print("Prints an object's details based on its class name and ID.")

    def do_destroy(self, cls_and_id):
        """Deletes an object based on its class name and ID.

        Arg:
            cls_and_id: class name and ID in string format.

        Usage:
            (hbnb) destroy <BaseModel> <id>
        """
        parsing_result = cmd.Cmd.parseline(self, cls_and_id)
        if parsing_result[0] is None:
            print("** class name missing **")
        elif parsing_result[0] not in self.cls_list:
            print("** class doesn't exist **")
        elif parsing_result[1] == "":
            print("** instance id missing **")

        else:
            my_dict = storage.all()
            if f"{parsing_result[0]}.{parsing_result[1]}" in my_dict:
                del my_dict[f"{parsing_result[0]}.{parsing_result[1]}"]
                for key, value in my_dict.items():
                    storage.all().update(my_dict)
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """Documentation for 'destroy' command."""
        print("Deletes a particular instance based on its class name and ID.")

    def do_all(self, cls):
        """Prints all instances stored either by class name or not.

        Arg:
            cls: Optional parameter class name of objects to be retrieved.

        Usage:
            (hbnb) all
            (hbnb) all ModelName
        """
        my_dict = storage.all()
        parsing_result = cmd.Cmd.parseline(self, cls)
        if parsing_result[0] is None:
            for value in my_dict.values():
                print(value)
        else:
            for key, value in my_dict.items():
                if f"{parsing_result[0]}" in key:
                    print(value)
                else:
                    print("** class doesn't exist **")

    def help_all(self):
        """Documentation for the 'all' interpretation command."""
        print("Prints all objects stored by class name or by presence.")

    def do_update(self, cls_id_attr_and_value):
        """Updates the attributes of a class object of given id.

        Arg:
            cls_id_attr_and_value: String format containing object's details.

        Usage:
            (hbnb) update <class name> <id> <attribute> <value>
        """
        parse = cmd.Cmd.parseline(self, cls_id_attr_and_value)
        if parse[0] is None:
            print("** class name missing **")
        elif parse[0] not in self.cls_list:
            print("** class doesn't exist **")
        elif parse[1] == "":
            print("** instance id missing **")
        elif len(parse[2].split(" ")) == 2:
            print("** attribute name missing **")
        elif len(parse[2].split(" ")) == 3:
            print("** value missing **")

        else:
            my_dict = storage.all()
            parse1 = parse[1].split(" ")
            if f"{parse[0]}.{parse1[0]}" in my_dict:
                new_dict = my_dict[f"{parse[0]}.{parse1[0]}"].to_dict()
                print(new_dict)
                new_dict[f"{parse1[1]}"] = parse1[2]
                print(new_dict)
                storage.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """Documentation for the 'update' command."""
        print("Sets a defined attribute to a specific value.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
