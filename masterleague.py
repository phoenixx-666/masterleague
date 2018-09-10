# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
import sys
from msvcrt import getch

import heroes
import roles
import match


FULL_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
epoch = datetime.utcfromtimestamp(0)
get_match_date = lambda (m, r): (datetime.strptime(m.date, FULL_DATE_FORMAT) - epoch).total_seconds()


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def query(**kwargs):
  warriors = kwargs.get('warriors')
  supports = kwargs.get('supports')
  assassins = kwargs.get('assassins')
  specialists = kwargs.get('specialists')
  specific_heroes = kwargs.get('specific_heroes')
  subroles = {subrole: kwargs[subrole] for subrole in heroes.SUBROLES if subrole in kwargs}
  franchises = {franchise: kwargs[franchise] for franchise in heroes.FRANCHISES if franchise in kwargs}
  melee = kwargs.get('melee')
  ranged = kwargs.get('ranged')
  date_from = kwargs.get('date_from')
  date_to = kwargs.get('date_to')
  res = set()
  matches = 0
  matches_no_mirror = 0
  wins = 0
    
  for m in match.MATCHES:
    match_date = datetime.strptime(m.date, FULL_DATE_FORMAT).date()
    if date_from and match_date < date_from or date_to and match_date > date_to:
      continue

    drafts = 0
    winner = False
    for draft in m.drafts:
      by_role = {roles.Role.WARRIOR: 0, roles.Role.SUPPORT: 0, roles.Role.ASSASSIN: 0, roles.Role.SPECIALIST: 0}
      by_subrole = {subrole: 0 for subrole in subroles}
      by_franchise = {franchise: 0 for franchise in franchises}
      n_melee = 0
      n_ranged = 0
      picked_heroes = []
      picked_hero_names = []
      
      # Collecting pick info
      for pick in draft['picks']:
        hero_id = pick['hero']
        picked_hero = heroes.get_by_id(hero_id)
        by_role[picked_hero.role] += 1
        for subrole in subroles:
          if picked_hero.name in heroes.SUBROLES[subrole]:
            by_subrole[subrole] += 1
        for franchise in franchises:
          if picked_hero.name in heroes.FRANCHISES[franchise]:
            by_franchise[franchise] += 1
        if picked_hero.name in heroes.RANGED:
          n_ranged += 1
        else:
          n_melee += 1
        picked_heroes.append(hero_id)
        picked_hero_names.append(picked_hero.name)
        
      # Checking basic roles
      if warriors is not None and by_role[roles.Role.WARRIOR] != warriors:
        continue
      if supports is not None and by_role[roles.Role.SUPPORT] != supports:
        continue
      if assassins is not None and by_role[roles.Role.ASSASSIN] != assassins:
        continue
      if specialists is not None and by_role[roles.Role.SPECIALIST] != specialists:
        continue
      
      # Checking subroles
      subrole_not_found = False
      for subrole in subroles:
        if by_subrole[subrole] != subroles[subrole]:
          subrole_not_found = True
          break
      if subrole_not_found:
        continue
      
      # Checking franchises
      franchise_not_found = False
      for franchise in franchises:
        if by_franchise[franchise] != franchises[franchise]:
          franchise_not_found = True
          break
      if franchise_not_found:
        continue
      
      # Checking specific heroes
      specific_hero_not_found = False
      if specific_heroes:
        for specific_hero in specific_heroes:
          try:
            hero_id = int(specific_hero)
          except ValueError:
            for picked_hero_name in picked_hero_names:
              if specific_hero.lower() in picked_hero_name.lower():
                break
            else:
              specific_hero_not_found = True
          else:
            if hero_id not in picked_heroes:
              specific_hero_not_found = True
              break
      if specific_hero_not_found:
        continue
        
      # Checking rangedness
      if ranged is not None and n_ranged != ranged:
        continue
      if melee is not None and n_melee != melee:
        continue
      
      # Checking if winner
      drafts += 1
      winner = draft['is_winner']
    if drafts:
      res.add((m, 'B' if drafts == 2 else 'W' if winner else 'L'))
      if drafts < 2:
        matches_no_mirror += 1
        if winner:
          wins += 1
  return sorted(res, key=get_match_date), len(res), float(wins) / matches_no_mirror if matches_no_mirror else 0


parser = argparse.ArgumentParser()
parser.add_argument('-w', metavar='N', type=int, nargs=1, dest='warriors')
parser.add_argument('-p', metavar='N', type=int, nargs=1, dest='supports')
parser.add_argument('-a', metavar='N', type=int, nargs=1, dest='assassins')
parser.add_argument('-s', metavar='N', type=int, nargs=1, dest='specialists')
for subrole in sorted(heroes.SUBROLES):
  parser.add_argument('--' + subrole, metavar='N', type=int, nargs=1, dest=subrole.replace('-', '_'), help='Number of heroes in the %s subrole' % subrole.replace('-', ' '))
for franchise in sorted(heroes.FRANCHISES):
  parser.add_argument('--' + franchise, metavar='N', type=int, nargs=1, dest=franchise)
parser.add_argument('--melee', metavar='N', nargs=1, type=int, dest='melee')
parser.add_argument('--ranged', metavar='N', nargs=1, type=int, dest='ranged')
parser.add_argument('--hero', metavar='N1 N2 N3...', nargs='*', dest='hero')
parser.add_argument('--pick-dates', action='store_true')
parser.add_argument('--fetch', action='store_true')
parser.add_argument('--date-from', metavar='YYYY-MM-DD', type=valid_date, nargs=1)
parser.add_argument('--date-to', metavar='YYYY-MM-DD', type=valid_date, nargs=1)


args = parser.parse_args(sys.argv[1:])


if args.fetch:
  from fetch import fetch
  fetch(False)
  sys.exit()


if args.pick_dates:
  pick_dates = {}
  pick_dates_list = []
  for m in sorted(match.MATCHES, key=lambda m: -(datetime.strptime(m.date, '%Y-%m-%dT%H:%M:%SZ') - epoch).total_seconds()):
    for draft in m.drafts:
      for pick in draft['picks']:
        hero_id = pick['hero']
        if hero_id not in pick_dates:
          date = datetime.strptime(m.date, '%Y-%m-%dT%H:%M:%SZ').date()
          pick_dates[hero_id] = date
          pick_dates_list.append((date, hero_id))
  
  for date, hero_id in pick_dates_list:
    print date, heroes.get_by_id(hero_id).name
  
  sys.exit()
    
kwargs = {}
if args.warriors:
  kwargs['warriors'] = args.warriors[0]
if args.supports:
  kwargs['supports'] = args.supports[0]
if args.assassins:
  kwargs['assassins'] = args.assassins[0]
if args.specialists:
  kwargs['specialists'] = args.specialists[0]

if args.tank:
  kwargs['tank'] = args.tank[0]
if args.bruiser:
  kwargs['bruiser'] = args.bruiser[0]
if args.healer:
  kwargs['healer'] = args.healer[0]
if args.support:
  kwargs['support'] = args.support[0]
if args.ambusher:
  kwargs['ambusher'] = args.ambusher[0]
if args.burst_damage:
  kwargs['burst-damage'] = args.burst_damage[0]
if args.sustained_damage:
  kwargs['sustained-damage'] = args.sustained_damage[0]
if args.siege:
  kwargs['siege'] = args.siege[0]
if args.utility:
  kwargs['utility'] = args.utility[0]
if args.stealth:
  kwargs['stealth'] = args.stealth[0]
if getattr(args, 'global'):
  kwargs['global'] = getattr(args, 'global')[0]

if args.warcraft:
  kwargs['warcraft'] = args.warcraft[0]
if args.starcraft:
  kwargs['starcraft'] = args.starcraft[0]
if args.diablo:
  kwargs['diablo'] = args.diablo[0]
if args.overwatch:
  kwargs['overwatch'] = args.overwatch[0]
if args.classic:
  kwargs['classic'] = args.classic[0]

if args.melee:
  kwargs['melee'] = args.melee[0]
if args.ranged:
  kwargs['ranged'] = args.ranged[0]

if args.hero:
  kwargs['specific_heroes'] = args.hero
  
if args.date_from:
  kwargs['date_from'] = args.date_from[0]
if args.date_to:
  kwargs['date_to'] = args.date_to[0]

res, matches, winrate = query(**kwargs)
print winrate * 100, '%'
print '%d matches in total' % matches

if matches > 100:
  print 'show last 100 matches [y/N]?'
  ch = getch()
  if ch.lower() == 'y':
    res = res[-100:]
  else:
    sys.exit()
for m, w in res:
  print m.url, w, datetime.strptime(m.date, '%Y-%m-%dT%H:%M:%SZ').date()
