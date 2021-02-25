from peewee import SqliteDatabase
from peewee import Model, TextField
import os
from os import path
from pathlib import Path



class Song(Model):
    search_term = TextField()
    video_id = TextField()

    class Meta:
        database = db
