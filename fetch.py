# -*- coding: utf-8 -*-

import argparse
import urllib2
import json
import sys
from time import sleep

def fetch(parse_args=True):
  if parse_args:
    parser = argparse.ArgumentParser()
    parser.add_argument('--from', metavar='N', type=int, nargs=1, default=1, dest='from')
    args = parser.parse_args(sys.argv[1:])

    ix = (lambda arg: arg[0] if isinstance(arg, list) else arg)(vars(args)['from'])
  else:
    ix = 1

  matches = []

  f = open('matches.json', 'r')
  matches = json.loads(f.read())
  f.close()

  match_ids = map(lambda m: m['id'], matches)

  url = 'https://api.masterleague.net/matches/?page=%d&format=json&page_size=25' % ix
  while True:
    print 'fetching page %d' % ix
    data = urllib2.urlopen(url)
    JSON = json.loads(data.read())
    data.close()
    finish = False
    for m in JSON['results']:
      if m['id'] in match_ids:
        finish = True
        break
      matches.append(m)
    if finish or not JSON['next']:
      break
    ix += 1
    url = JSON['next']
    sleep(2)

  f = open('matches.json', 'w')
  f.write(json.dumps(matches, indent=2))
  f.close()

if __name__ == '__main__':
  fetch()
