#!/usr/bin/python3
"""
Module base_model
"""


import uuid
import datetime
import models


class BaseModel:
    """class base basemodel that define
    all atribute and method
    """
    def __init__(self, *args, **kwargs):
        """ Now it’s time to re-create an instance
        with this dictionary representation. """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
                if key in ["created_at", "updated_at"]:
                    fmt = "%Y-%m-%dT%H:%M:%S.%f"
                    new_time = datetime.datetime.strptime(value, fmt)
                    setattr(self, key, new_time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """str funtion that print
        [<class name>]: class name
        (<self.id>): print id
        <self.__dict__> print dict_
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """method
        to: updates the public instance attribute
        with current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ method that
        to: returns a dictionary containing all keys/values
        {'created_at': '2017-09-28T21:05:54.119572'}
        of __dict__ of the instance
        """
        value_dict = self.__dict__.copy()
        value_dict["__class__"] = self.__class__.__name__
        fmt2 = "%Y-%m-%dT%H:%M:%S.%f%z"
        if "created_at" in value_dict.keys():
            value_dict["created_at"] = self.created_at.strftime(fmt2)
        if "updated_at" in value_dict.keys():
            value_dict["updated_at"] = self.updated_at.strftime(fmt2)

        return value_dict
