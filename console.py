#!/usr/bin/python3
"""my module console.py"""
import cmd
import os
import models
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import classes
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """mi class"""
    intro = "Simple shell yourwelcome wilson Linux."
    last_output = ''
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Command to Creates a new instance of a class"""
        lista = shlex.split(arg)
        if len(lista) == 0:
            print("** class name missing **")

        elif lista[0] in classes:
            instance = classes[lista[0]]()
            print(instance.id)
            instance.save()
        else:
            # from models.__init__ import storage
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Command to Prints the string
        representation of an instance"""
        lista = shlex.split(arg)
        if len(lista) == 0:
            print("** class name missing **")

        elif lista[0] in classes:
            if len(lista) > 1:
                key = lista[0] + "." + lista[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based
        on the class name and id"""
        lista = shlex.split(arg)
        if len(lista) == 0:
            print("** class name missing **")

        elif lista[0] in classes:
            if len(lista) > 1:
                key = lista[0] + "." + lista[1]
                if key in models.storage.all().keys():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        lista = shlex.split(arg)
        obj_list = []
        if len(lista) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            obj_str = "[" + ", ".join(obj_list) + "]"
            print(obj_str)
        elif lista[0] in classes:
            for key, value in models.storage.all().items():
                if lista[0] in key:
                    obj_list.append(str(value))
            obj_str = "[" + ", ".join(obj_list) + "]"
            print(obj_str)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)."""
        lista = shlex.split(arg)
        data_update = ["id", "created_at", "update_at"]
        objects = models.storage.all()

        if len(lista) == 0:
            print("** class name missing **")

        elif lista[0] not in classes:
            print("** class doesn't exist **")

        elif len(lista) == 1:
            print("** instance id missing **")

        else:
            key = lista[0] + "." + lista[1]
            if key not in models.storage.all().keys():
                print("** no instance found **")
            elif len(lista) == 2:
                print("** attribute name missing **")
            elif len(lista) == 3:
                print("** value missing **")
            elif lista[2] not in data_update:
                obj = objects[key]
                obj.__dict__[lista[2]] = lista[3]
                # obj.updated_at = datetime.now()
                obj.save()

#    def __init__(self):
#        cmd.Cmd.__init__(self)
#        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """to exit the program"""
        print()
        exit()

#   def do_exit(self, arg):
#        """end of file"""
#        return True

    def do_shell(self, arg):
        """run a shell command"""
        output = os.popen(arg).read()
        print(output)

    def emptyline(self):
        """ overwriting the emptyline method """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
