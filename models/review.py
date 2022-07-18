#!/usr/bin/python3
"""defines review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review"""
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
