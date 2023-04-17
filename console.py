#!/usr/bin/python3
""" module for entry point of the command interpreter """
import cmd
import shlex
import models
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    prompt = "(hbnb) "
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    cmds = ["all", "count", "show", "destroy", "update"]

    def do_quit(self, line):
        """ quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Ctrl-D command to exit the program """
        print()
        return True

    def emptyline(self):
        """ an empty line + ENTER will not execute anything """
        pass

    def do_create(self, line):
        """ creates a new instance, saves it, and prints id """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, cls_and_id):
        """prints the str repr of an instance with class name and id"""
        cls_name = self.parseline(cls_and_id)[0]
        cls_id = self.parseline(cls_and_id)[1]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.cls:
            print("** class doesn't exist **")
        elif cls_id is None:
            print("** instance id missing **")
        else:
            key = cls_name + "." + cls_id
            obj = models.storage.all().get(key, "** no instance found **")
            print(obj)

    def do_destroy(self, cls_and_id):
        """ deletes an instance based on the class name and id """
        cls_name = self.parseline(cls_and_id)[0]
        cls_id = self.parseline(cls_and_id)[1]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in self.cls:
            print("** class doesn't exist **")
        elif cls_id is None:
            print("** instance id missing **")
        else:
            key = cls_name + "." + cls_id
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, class_name):
        """ prints all string representation of all instances """
        cls_name = self.parseline(class_name)[0]
        objs = models.storage.all()
        if cls_name is None:
            for value in objs.values():
                print(str(value))
        elif cls_name in self.cls:
            keys = objs.keys()
            for key in keys:
                if key.startswith(cls_name):
                    print(str(objs[key]))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ updates an instance based on the class name and id """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print("** class name missing **")
        elif args[0] not in self.cls:
            print("** class doesn't exist **")
        elif args_size == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif args_size == 2:
                print("** attribute name missing **")
            elif args_size == 3:
                print("** value missing **")
            else:
                if args[3].isdigit():
                    args[3] = int(args[3])
                elif args[3].replace(".", "", 1).isdigit():
                    args[3] = float(args[3])
                setattr(obj, args[2], args[3])
                setattr(obj, "updated_at", datetime.now())
                models.storage.save()

    def do_count(self, class_name):
        """ prints the number of instances of a class """
        cls_name = self.parseline(class_name)[0]
        counter = 0
        if cls_name is None:
            print("** class name missing **")
        for keys in models.storage.all().keys():
            if keys.split(".")[0] == cls_name:
                counter += 1
        print(counter)

    def default(self, inp):
        """ converts custom user input into commands """
        parsed_inp = self.default_error_check(inp)
        if parsed_inp is None:
            return
        cls_name, cmd, args = parsed_inp
        if cmd == "all":
            return self.do_all(cls_name)
        if cmd == "count":
            return self.do_count(cls_name)
        if cmd == "show":
            return self.do_show(cls_name + " " + args)
        if cmd == "destroy":
            return self.do_destroy(cls_name + " " + args)
        if cmd == "update":
            if "{" in args and "}" in args:
                self.evaluate_kwargs(cls_name, args)
            else:
                self.evaluate_args(cls_name, args)

    def default_error_check(self, inp):
        """ checks for errors in input for default method """
        if "." not in inp:
            return(print("** invalid input **"))
        cls_name = inp.split(".")[0]
        if cls_name not in self.cls:
            return(print("** class doesn't exist **"))
        idx = inp.index(".")
        cmd = inp[idx + 1:]
        if "(" not in cmd and ")" not in cmd:
            return(print("** invalid input **"))
        cmd_left = cmd.split("(")[0]
        cmd_right = cmd.split("(")[-1][:-1]
        if cmd_left not in self.cmds:
            return(print("** invalid command **"))
        return [cls_name, cmd_left, cmd_right]

    def evaluate_kwargs(self, cls_name, cmd):
        """ converts string to correct format for update method """
        idx = cmd.index(",")
        cls_id = cmd[:idx].replace("\"", "")
        string_d = cmd[idx + 1:]
        d = eval(string_d)
        for k, v in d.items():
            arg = cls_name + " " + cls_id + " " + k + " " + '"' + str(v) + '"'
            self.do_update(arg)

    def evaluate_args(self, cls_name, cmd):
        """ converts string to correct format for update method """
        arg = cls_name + " "
        for i in cmd.split(", ")[:-1]:
            arg += i.replace("\"", "") + " "
        arg += cmd.split(", ")[-1]
        self.do_update(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
