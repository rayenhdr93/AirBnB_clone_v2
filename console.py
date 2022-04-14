#!/usr/bin/python3
"""The main command line for the backend of the airbnb project."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Cmd SubClass."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program."""
        return True

    @staticmethod
    def check_type(value):
        """Check Value type."""
        arg = ""
        if value[0] == '"' and value[-1] == '"':
            for i in range(1, len(value)-1):
                if value[i] == '"' and value[i-1] != '\\':
                    return None
                if value[i] == "_":
                    arg += " "
                else:
                    arg += value[i]
            return arg
        elif '.' in value and RepresentsFloat(value):
            return float(value)
        elif RepresentsInt(value):
            return int(value)
        else:
            return None

    def do_create(self, args):
        """
        Create a new instance of Baseclass and save it.

        Usage: create [Class Name]
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if class_nexist(args[0]):
            print("** class doesn't exist **")

        new_instance = eval(args[0])()
        args.pop(0)
        for arg in args:
            arg = arg.split('=')
            if len(arg) != 2:
                continue
            key = arg[0]
            value = arg[1]
            value = self.check_type(value)
            if value is None:
                continue
            else:
                setattr(new_instance, key, value)

        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show representation of object by id.

        Usage: show [class name] [id]
        """
        obj = arg.split(' ')

        if arg == "":
            print("** class name missing **")
        else:
            if class_nexist(obj[0]):
                print("** class doesn't exist **")
            elif len(obj) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                obj = obj[0]+'.'+obj[1]
                if obj in objs:
                    print(objs[obj])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete instance of class by idselfself.

        Usage: destro [class] [id]
        """
        obj = arg.split(' ')

        if arg == "":
            print("** class name missing **")
        else:
            if class_nexist(obj[0]):
                print("** class doesn't exist **")
            elif len(obj) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                obj = obj[0]+'.'+obj[1]
                if obj in objs:
                    del objs[obj]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Show all objects.

        Usage: all [[class]]
        """
        objs = storage.all()
        obj_str = []

        if arg == "":
            for obj in objs:
                obj_str.append(str(objs[obj]))
            print(obj_str)

        else:
            if class_nexist(arg):
                print("** class doesn't exist **")
            else:
                for obj in objs:
                    if objs[obj].to_dict()['__class__'] == arg:
                        obj_str.append(str(objs[obj]))
                print(obj_str)

    def do_update(self, arg):
        """
        Upadate the object with attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(' ')

        if arg == "":
            print("** class name missing **")

        elif class_nexist(args[0]):
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            objs = storage.all()
            obj = args[0] + '.' + args[1]
            if obj in objs:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    last = args[len(args) - 1]
                    value = args[3]
                    attribute = args[2]
                    if args[3][0] == "\"" and\
                            last[len(last) - 1] == "\"" and len(args) > 4:
                        for i in range(4, len(args)):
                            value += ' ' + args[i]
                    else:
                        value = args[3]
                    value = value.strip("\"")
                    attribute = attribute.strip("\"")
                    if hasattr(objs[obj], attribute):
                        if type(getattr(objs[obj], attribute)) is str:
                            value = str(value)
                        elif type(getattr(objs[obj], attribute)) is int:
                            value = int(value)
                        elif type(getattr(objs[obj], attribute)) is float:
                            value = float(value)

                    setattr(objs[obj], attribute, value)
                    objs[obj].save()
            else:
                print("** no instance found **")


def class_nexist(_class):
    """Check if class exists."""
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]
    return _class not in classes


def RepresentsInt(s):
    """Check is string can be int."""
    try:
        int(s)
        return True
    except ValueError:
        return False


def RepresentsFloat(s):
    """Check is string can be float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
