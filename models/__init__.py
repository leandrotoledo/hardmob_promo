#!/usr/bin/env python
from pony.orm import Database

db = Database()

from .post import Post

db.bind('sqlite', '../db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

__all__ = ('Post',)
