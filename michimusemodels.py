from peewee import *
import os

db = SqliteDatabase(os.path.expanduser('~/.config/michimuse.sqlite'))

class Track(Model):
  path = CharField()
  title = CharField()
  artist = CharField()
  album = CharField()
  def __str__(self):
    return "%s by %s from %s [%s]" % (self.title, self.artist, self.album, self.path)
  class Meta:
    database = db

Track.create_table(fail_silently=True)
