#!/usr/bin/env python3
"""
Class Basemodel that define all common attributes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    defines a Basemodel class
    """

    def __init__(self, *arg, **kwargs):
        """initializes the Basemodel"""
        if arg:
            pass
        """self.id = str(uuid4())"""
        self.created_at = datetime.isoformat(datetime.now())
        self.updated_at = datetime.isoformat(datetime.now())
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """returns the print of the basemodel"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """uptade with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        return new_dict