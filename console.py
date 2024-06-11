#!/usr/bin/python3
"""
'console' is the entry point to the AirBnB console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Collection of attributes and methods enabling command interpretation.

    Parent Class:
        Cmd: Provides class fields for command manipulation.
    """

    prompt = "(hbnb) "
    intro = "\nCurrently running: AirBnb_clone Command interpreter.\n"

    def do_quit(self, line):
        """Executes for input command 'quit'."""
        return (True)

    def help_quit(self):
        """Documentation for help input command linked to auit command."""
        print("When called, will exit/terminate the program.")

    def do_EOF(self, line):
        """Executes to exit cmdloop()."""
        print()
        return (True)

    def help_EOF(self):
        """Documentation pf End Of File signals as input (i.e. CTRL-D)"""
        print("Handles 'CTRL-D' as input command and terminates execution.")

    def empty_list(self):
        """Executes when input command is 'an empty string'."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
