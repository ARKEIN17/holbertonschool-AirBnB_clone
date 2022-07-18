#!/usr/bin/python3
"""defines a class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines user by various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
