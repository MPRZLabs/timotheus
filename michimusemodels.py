from peewee import *
import os

db = SqliteDatabase(os.path.expanduser('~/.config/michimuse.sqlite'))

class Track(Model):
  path = CharField()
  title = CharField()
  artist = CharField()
  album = CharField()
  def __str__(self):
    ttl = self.title
    if len(ttl) < 1:
      ttl = ":::"
    ats = self.artist
    if len(ats) < 1:
      ats = ":::"
    abm = self.album
    if len(abm) < 1:
      abm = ":::"
    return "%s by %s from %s" % (ttl, ats, abm)
  def __repr__(self):
    return "[Track %s]" % self.__str__()
  class Meta:
    database = db

Track.create_table(fail_silently=True)
