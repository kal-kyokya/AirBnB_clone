#!/usr/bin/python3
"""
'console' is the entry point to the AirBnB console
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Collection of attributes and methods enabling command interpretation.

    Parent Class:
        Cmd: Provides class fields for command manipulation.
    """

    prompt = "(hbnb) "

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
        elif parsing_result[0] != "BaseModel":
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
        elif parsing_result[0] != "BaseModel":
            print(f"{parsing_result[0]}: ", "** class doesn't exist **")
        elif parsing_result[1] == "BaseModel":
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
