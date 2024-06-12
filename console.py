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
        """
        return (True)

    def help_quit(self):
        """Documentation for help input command linked to auit command."""
        print("When called, will exit/terminate the program.")

    def do_EOF(self, line):
        """Executes to exit cmdloop().

        Arg:
            line: Potential input parameter to the 'quit' command.
        """
        print()
        return (True)

    def help_EOF(self):
        """Documentation pf End Of File signals as input (i.e. CTRL-D)"""
        print("Handles 'CTRL-D' as input command and terminates execution.")

    def emptyline(self):
        """Executes when input command is 'an empty string'."""
        pass

    def do_create(self, cls_type=None):
        """Initializes an object of specific class type.

        Arg:
            cls_type: Desired class type for object to be constructed.
        """
        if cls_type is None:
            print("** class name missing **")
        elif cls_type != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = eval(cls_type)()
            storage.new(obj)
            storage.save()
            print(f"{obj.id}")

    def help_create(self):
        """Documentation for the 'create' interpreter command."""
        print("Constructs/Initializes an object of defined class type.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
