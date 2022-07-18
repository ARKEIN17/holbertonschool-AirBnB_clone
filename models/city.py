#!/usr/bin/python3
"""Defines a city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """city"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
