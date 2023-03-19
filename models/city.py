#!/usr/bin/python3
"""Module to define City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Defining Class representing a City."""
    state_id = ""
    name = ""
