#!/usr/bin/env python3

from pymarkovchain import MarkovChain
import twitter, os, json, sys

class GenP(object):
  def __init__(self, performer, person, spec=False):
    self.performer = performer
    self.person = person
    self.spec = spec

class GenV(object):
  def __init__(self, present, past=None, presentspec=None, future=None, subject=True):
    self.present = present
    if past is None:
      self.past = "%sd" % self.present
    else:
      self.past = past
    if presentspec is None:
      self.presentspec = "%ss" % self.present
    else:
      self.presentspec = presentspec
    if future is None:
      self.future = self.present
    else:
      self.future = future
    self.subject = subject

class AutoGen(object):
  def __init__(self):
    self.performers = [GenP("I",1),GenP("You",2),GenP("He",3,True),GenP("She",3,True),GenP("It",3,True),GenP("We",1),GenP("They",3),GenP("Someone",3,True),GenP("Somebody",3,True),GenP("Anyone",3,True),GenP("Anybody",3,True),GenP("Everyone",3,True),GenP("Everybody",3,True),GenP("World",3,True),GenP("The world",3,True),GenP("Cake",3,True)]
    self.verbs = [GenV("like"),GenV("do","did","does",subject=False),GenV("hate"),GenV("dislike"),GenV("love"),GenV("do not mind","did not mind","does not mind","not mind"),GenV("think","thought", subject=False),GenV("think about","thought about","thinks about"),GenV("find","found"),GenV("find out about","found out about","finds out about"),GenV("have","had","has"),GenV("fall in love with","fell in love with","falls in love with"),GenV("bake"),GenV("get baked by","got baked by","gets baked by"),GenV("wake up","woke up","wakes up",subject=False),GenV("fly","flew","flies",subject=False),GenV("compile"),GenV("read","read")]
    self.subjects = ["me","you","him","her","it","us","them","pancakes","bicycles","Twitter","video games","science-fiction movies","Minecraft","Braid","anarchy","cat","cats","Linux","Windows","Microsoft","Apple","a car","Jimmy","big giant circles","Facebook","Steve"]
  def gen(self):
    for verb in self.verbs:
      for perf in self.performers:
        if verb.subject:
          for subj in self.subjects:
            if perf.spec:
              print("%s %s %s." % (perf.performer, verb.presentspec, subj))
            else:
              print("%s %s %s." % (perf.performer, verb.present, subj))
            print("%s %s %s." % (perf.performer, verb.past, subj))
            print("%s did not %s %s." % (perf.performer, verb.present, subj))
            print("%s will %s %s." % (perf.performer, verb.future, subj))
            print("%s will not %s %s." % (perf.performer, verb.future, subj))
        else:
          if perf.spec:
            print("%s %s." % (perf.performer, verb.presentspec))
          else:
            print("%s %s." % (perf.performer, verb.present))
          print("%s %s." % (perf.performer, verb.past))
          print("%s did not %s." % (perf.performer, verb.present))
          print("%s will %s." % (perf.performer, verb.future))
          print("%s will not %s." % (perf.performer, verb.future))

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
