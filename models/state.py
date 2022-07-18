#!/usr/bin/python3
"""defines state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
