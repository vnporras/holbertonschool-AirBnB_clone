#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter:
"""
import os.path
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ Simple command processor example. """
    prompt = "(hbnb) "
    __file_path = "file.json"

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name_and_id = arg.split()            
            eval(class_name_and_id[0])()        

            if len(class_name_and_id) != 2:
                print("** instance id missing **")
                return
            
            id = class_name_and_id[1]

            try:
                with open(self.__file_path, "r", encoding="utf-8") as file:                
                    object_string = None
                    for key, value in json.load(file).items():
                        if key == f"{class_name_and_id[0]}.{id}":
                            object_string = value

                    if object_string == None:
                        print("** no instance found **")
                        return

                    print(f"{[class_name_and_id[0]]} ({id}) {object_string}")
            except FileNotFoundError:
                pass
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
   
        try:
            class_name_and_id = arg.split()
            if len(class_name_and_id) != 2:
                print("** instance id missing **")
                return

            try:
                with open(self.__file_path, "r", encoding="utf-8") as file:
                    objects = json.load(file)
                    object_key = f"{class_name_and_id[0]}.{class_name_and_id[1]}"
                    if object_key not in objects:
                        print("** no instance found **")
                        return
                    
                    del objects[object_key]
                
                with open(self.__file_path, "w", encoding="utf-8") as file:
                    json.dump(objects, file)
            except FileNotFoundError:
                print("** class doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = arg
            eval(class_name)()
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
        except NameError:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the console"""
        sys.exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()