#!/usr/bin/env python3

from pymarkovchain import MarkovChain
import twitter, os, json, sys

class AutoGen(object):
  def __init__(self):
    with open("margenperformers.json") as file:
      self.performers = json.loads(file.read())
    with open("margenverbs.json") as file:
      self.verbs = json.loads(file.read())
    with open("margensubjects.json") as file:
      self.subjects = json.loads(file.read())
  def gen(self):
    for verb in self.verbs:
      for perf in self.performers:
        if verb['use-subject']:
          for subj in self.subjects:
            if perf['special']:
              print("%s %s %s." % (perf['performer'], verb['present-special'], subj))
            else:
              print("%s %s %s." % (perf['performer'], verb['present'], subj))
            print("%s %s %s." % (perf['performer'], verb['past'], subj))
            print("%s did not %s %s." % (perf['performer'], verb['present'], subj))
            print("%s will %s %s." % (perf['performer'], verb['future'], subj))
            print("%s will not %s %s." % (perf['performer'], verb['future'], subj))
        else:
          if perf['special']:
            print("%s %s." % (perf['performer'], verb['present-special']))
          else:
            print("%s %s." % (perf['performer'], verb['present']))
          print("%s %s." % (perf['performer'], verb['past']))
          print("%s did not %s." % (perf['performer'], verb['present']))
          print("%s will %s." % (perf['performer'], verb['future']))
          print("%s will not %s." % (perf['performer'], verb['future']))

class Michiov(object):
  def __init__(self, autogen=True, markovdb=os.path.expanduser("~/markov"), twcreds=os.path.expanduser("~/.michiov_twitter_credentials"),twappcreds=os.path.expanduser("~/.michiov_twitter_appdata")):
    self.mc = MarkovChain(markovdb)
    self.reload()
    if not os.path.exists(twappcreds):
      print("Lack of app creds")
      sys.exit(1)
    twcons = json.loads(open(twappcreds).read())
    conskey = twcons['key']
    conssec = twcons['secret']
    while not os.path.exists(twcreds):
      twitter.oauth_dance("MPRZ Tech Labs", conskey, conssec, twcreds)
    oauth_token, oauth_secret = twitter.read_token_file(twcreds)
    self.t = twitter.Twitter(auth=twitter.OAuth(oauth_token, oauth_secret, conskey, conssec))
  def should(self):
    ret = input("Should I send it? (y/N) ")
    return ("y" in ret or "Y" in ret)
  def qas(self):
    idea = self.mc.generateString()
    print("Generated: %s" % idea)
    if self.should():
      self.t.statuses.update(status=idea)
  def loop(self):
    try:
      while True:
        self.qas()
        #self.reload()
    except KeyboardInterrupt:
      pass
  def reload(self):
    with open("markovpredb.txt") as file:
      self.mc.generateDatabase(file.read())

if __name__ == '__main__':
  Michiov().loop()
