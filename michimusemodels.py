from peewee import *
import os

db = SqliteDatabase(os.path.expanduser('~/.config/michimuse.sqlite'))

class Track(Model):
  path = CharField()
  title = CharField()
  artist = CharField()
  album = CharField()
  def get_title(self):
    if len(self.title) < 1:
      return ":::"
    else:
      return self.title
  def get_album(self):
    if len(self.album) < 1:
      return ":::"
    else:
      return self.album
  def get_artist(self):
    if len(self.artist) < 1:
      return ":::"
    else:
      return self.artist
  def __str__(self):
    return "%s by %s from %s" % (self.get_title(), self.get_artist(), self.get_album())
  def __repr__(self):
    return "[Track %s]" % self.__str__()
  class Meta:
    database = db

Track.create_table(fail_silently=True)
