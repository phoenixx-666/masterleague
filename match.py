# -*- coding: utf-8 -*-

import json

class Match:
  def __init__(self, **kwargs):
    self.match_id = kwargs.pop('id')
    for key, value in kwargs.iteritems():
      setattr(self, key, value)

f = open('matches.json', 'r')
MATCHES = map(lambda m: Match(**m), json.loads(f.read()))
f.close()
