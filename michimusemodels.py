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

class Tag(Model):
  name = CharField()
  def tag_by_query(self, query):
    for track in query:
      Tagged.create(track = track, tag = self)
  def tag_by_artist(self, artist):
    for track in Track.select().where(Track.artist.contains(artist)):
      Tagged.create(track = track, tag = self)
  def tag_by_path(self, path):
    for track in Track.select().where(Track.path.contains(path)):
      Tagged.create(track = track, tag = self)
  class Meta:
    database = db

class Tagged(Model):
  track = ForeignKeyField(Track)
  tag = ForeignKeyField(Tag, related_name='marks')
  class Meta:
    database = db

def hunt_tags():
  for tag1 in Tagged.select():
    print(tag1.id)
    for tag2 in Tagged.select():
      if tag1.tag == tag2.tag and tag1.track == tag2.track:
        if tag1.id != tag2.id:
          print("-", end='')
          tag2.delete_instance()
          return False
        else:
          print(":", end='')
      else:
        print(".", end='')
    print()
  return True

if __name__ == '__main__':
  Track.create_table(fail_silently=False)
  Tag.create_table(fail_silently=False)
  Tagged.create_table(fail_silently=False)
else:
  Track.create_table(fail_silently=True)
  Tag.create_table(fail_silently=True)
  Tagged.create_table(fail_silently=True)
