#!/usr/bin/python3
"""my module console.py"""
import cmd
import os
import models 
from models.base_model import BaseModel


classes = {'BaseModel' : BaseModel}
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
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self):
        """Deletes an instance based
        on the class name and id"""
        lista = arg.split()
        if len(lista)== 0:
            print("** class name missing **")

        if lista[0] in classes:
            if len(lista) > 1:
                key = lista[0] + "." + lista[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self):
        """Prints all string representation of all instances
        based or not on the class name"""



    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """to exit the program"""
        return True

    def do_exit(self, arg):
        """end of file"""
        return True

    def do_shell(self, arg):
        """run a shell command"""
        output = os.popen(arg).read()
        print(output)



if __name__ == '__main__':
    HBNBCommand().cmdloop()

