#!/usr/bin/python3
"""defines amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize """
        super().__init__(*args, **kwargs)