#!/usr/bin/python3
"""my module console.py"""
import cmd
import os
import models 
from models.base_model import BaseModel


classes = {'BaseModel' : BaseModel, "Cuadrado": "Cuadrado"}
class HBNBCommand(cmd.Cmd):
    """mi class"""
    intro = "Simple shell yourwelcome wilson Linux."
    last_output = ''

    def do_create(self, arg):
        """Command to Creates a new instance of a class"""
        lista = arg.split()
        if len(lista)== 0:
            print("** class name missing **")

        if lista[0] in classes:
            instance = classes[lista[0]]()
            print(instance.id)
            instance.save()
        else:
# from models.__init__ import storage
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Command to Prints the string
        representation of an instance"""
        lista = arg.split()
        if len(lista)== 0:
            print("** class name missing **")

        if lista[0] in classes:
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
        lista = arg.split()
        if len(lista)== 0:
            print("** class name missing **")

        if lista[0] in classes:
            if len(lista) > 1:
                key = lista[0] + "." + lista[1]
                if key in models.storage.all().keys():
                    del models.storage.all()[key]
                    models.storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        lista = arg.split()
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
            print("** class doesn't exists **")


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """to exit the program"""
        return True

#   def do_exit(self, arg):
#        """end of file"""
#        return True

    def do_shell(self, arg):
        """run a shell command"""
        output = os.popen(arg).read()
        print(output)

    def emptyline(self):
        """ overwriting the emptyline method """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()

