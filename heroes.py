# -*- coding: utf-8 -*-

import json
from roles import Role as R

class Hero:
  def __init__(self, **kw):
    self.hero_id = kw['id']
    self.name = kw['name']
    self.role = kw['role']
   
  def __repr__(self):
    return '<Hero: "%s" (%d)>' % (self.name, self.hero_id)

HEROES = [
  Hero(id=1, name='The Butcher', role=R.ASSASSIN),
  Hero(id=2, name='Johanna', role=R.WARRIOR),
  Hero(id=3, name="Kael'thas", role=R.ASSASSIN),
  Hero(id=4, name='Sylvanas', role=R.SPECIALIST),
  Hero(id=5, name='The Lost Vikings', role=R.SPECIALIST),
  Hero(id=6, name='Thrall', role=R.ASSASSIN),
  Hero(id=7, name='Jaina', role=R.ASSASSIN),
  Hero(id=8, name="Anub'arak", role=R.WARRIOR),
  Hero(id=9, name='Azmodan', role=R.SPECIALIST),
  Hero(id=10, name='Chen', role=R.WARRIOR),
  Hero(id=11, name='Rehgar', role=R.SUPPORT),
  Hero(id=12, name='Zagara', role=R.SPECIALIST),
  Hero(id=13, name='Murky', role=R.SPECIALIST),
  Hero(id=14, name='Brightwing', role=R.SUPPORT),
  Hero(id=15, name='Li Li', role=R.SUPPORT),
  Hero(id=16, name='Tychus', role=R.ASSASSIN),
  Hero(id=17, name='Stitches', role=R.WARRIOR),
  Hero(id=18, name='Arthas', role=R.WARRIOR),
  Hero(id=19, name='Diablo', role=R.WARRIOR),
  Hero(id=20, name='Tyrael', role=R.WARRIOR),
  Hero(id=21, name='E.T.C.', role=R.WARRIOR),
  Hero(id=22, name='Sonya', role=R.WARRIOR),
  Hero(id=23, name='Muradin', role=R.WARRIOR),
  Hero(id=24, name='Kerrigan', role=R.ASSASSIN),
  Hero(id=25, name='Nova', role=R.ASSASSIN),
  Hero(id=26, name='Falstad', role=R.ASSASSIN),
  Hero(id=27, name='Valla', role=R.ASSASSIN),
  Hero(id=28, name='Illidan', role=R.ASSASSIN),
  Hero(id=29, name='Raynor', role=R.ASSASSIN),
  Hero(id=30, name='Zeratul', role=R.ASSASSIN),
  Hero(id=31, name='Uther', role=R.SUPPORT),
  Hero(id=32, name='Malfurion', role=R.SUPPORT),
  Hero(id=33, name='Tassadar', role=R.SUPPORT),
  Hero(id=34, name='Tyrande', role=R.SUPPORT),
  Hero(id=35, name='Nazeebo', role=R.SPECIALIST),
  Hero(id=36, name='Gazlowe', role=R.SPECIALIST),
  Hero(id=37, name='Abathur', role=R.SPECIALIST),
  Hero(id=38, name='Sgt. Hammer', role=R.SPECIALIST),
  Hero(id=39, name='Kharazim', role=R.SUPPORT),
  Hero(id=40, name='Leoric', role=R.WARRIOR),
  Hero(id=41, name='Rexxar', role=R.WARRIOR),
  Hero(id=42, name='Lt. Morales', role=R.SUPPORT),
  Hero(id=43, name='Artanis', role=R.WARRIOR),
  Hero(id=44, name='Cho', role=R.WARRIOR),
  Hero(id=45, name='Gall', role=R.ASSASSIN),
  Hero(id=46, name='Lunara', role=R.ASSASSIN),
  Hero(id=47, name='Greymane', role=R.ASSASSIN),
  Hero(id=48, name='Li-Ming', role=R.ASSASSIN),
  Hero(id=49, name='Xul', role=R.SPECIALIST),
  Hero(id=50, name='Dehaka', role=R.WARRIOR),
  Hero(id=51, name='Tracer', role=R.ASSASSIN),
  Hero(id=52, name='Chromie', role=R.ASSASSIN),
  Hero(id=53, name='Medivh', role=R.SPECIALIST),
  Hero(id=54, name="Gul'dan", role=R.ASSASSIN),
  Hero(id=55, name='Auriel', role=R.SUPPORT),
  Hero(id=56, name='Alarak', role=R.ASSASSIN),
  Hero(id=57, name='Zarya', role=R.WARRIOR),
  Hero(id=58, name='Samuro', role=R.ASSASSIN),
  Hero(id=59, name='Varian', role=R.WARRIOR),
  Hero(id=60, name='Ragnaros', role=R.ASSASSIN),
  Hero(id=61, name="Zul'jin", role=R.ASSASSIN),
  Hero(id=62, name='Valeera', role=R.ASSASSIN),
  Hero(id=63, name='Lucio', role=R.SUPPORT),
  Hero(id=64, name='Probius', role=R.SPECIALIST),
  Hero(id=65, name='Cassia', role=R.ASSASSIN),
  Hero(id=66, name='Genji', role=R.ASSASSIN),
  Hero(id=67, name='D.Va', role=R.WARRIOR),
  Hero(id=68, name='Malthael', role=R.ASSASSIN),
  Hero(id=69, name='Stukov', role=R.SUPPORT),
  Hero(id=70, name='Garrosh', role=R.WARRIOR),
  Hero(id=71, name="Kel'Thuzad", role=R.ASSASSIN),
  Hero(id=72, name='Ana', role=R.SUPPORT),
  Hero(id=73, name='Junkrat', role=R.ASSASSIN),
  Hero(id=74, name='Alexstrasza', role=R.SUPPORT),
  Hero(id=75, name='Hanzo', role=R.ASSASSIN),
  Hero(id=76, name='Blaze', role=R.WARRIOR),
  Hero(id=77, name='Maiev', role=R.ASSASSIN),
  Hero(id=78, name='Fenix', role=R.ASSASSIN),
  Hero(id=79, name='Deckard', role=R.SUPPORT),
  Hero(id=80, name='Yrel', role=R.WARRIOR),
  Hero(id=81, name='Whitemane', role=R.SUPPORT),
  Hero(id=82, name='Mephisto', role=R.ASSASSIN),
]


SUBROLES = {
  "tank":
    ["Rexxar", "Anub'arak", "Arthas", "Diablo", "Johanna", "D.Va", "E.T.C.", "Stitches",
     "Muradin", "Garrosh", "Cho", "Blaze", "Tyrael", "Varian", "Yrel"],
  "bruiser": ["Sonya", "Artanis", "Chen", "Dehaka", "Leoric", "Zarya",],
  "healer":
    ["Ana", "Alexstrasza", "Rehgar", "Uther", "Kharazim", "Li Li", "Lucio", "Malfurion",
    "Stukov", "Brightwing", "Lt. Morales", "Auriel", "Deckard", "Whitemane"],
  "support": ["Tyrande", "Tassadar", "Medivh"],
  "ambusher": ["The Butcher", "Samuro", "Kerrigan", "Alarak", "Nova", "Valeera", "Zeratul"],
  "burst-damage": ["Jaina", "Kael'thas", "Chromie", "Li-Ming", "Kel'Thuzad"],
  "sustained-damage":
    ["Malthael", "Tracer", "Nazeebo", "Greymane", "Ragnaros", "Valla", "Illidan", "Cassia",
     "Lunara", "Zul'jin", "Falstad", "Gul'dan", "Raynor", "Thrall", "Tychus", "Genji",
     "Gall", "Junkrat", "Hanzo", "Maiev", "Fenix", "Mephisto"],
  "siege": ["Xul", "Azmodan", "Zagara", "Gazlowe", "Sgt. Hammer", "Sylvanas", "Probius"],
  "utility": ["Murky", "The Lost Vikings", "Abathur"],
  "stealth": ["Nova", "Samuro", "Valeera", "Zeratul"],
  "global": ["Abathur", "Brightwing", "Dehaka", "Falstad"],
}


RANGED = ["Rexxar", "D.Va", "Li Li", "Lucio", "Malfurion", "Brightwing", "Lt. Morales", "Auriel",
          "Tyrande", "Tassadar", "Medivh", "Nova", "Jaina", "Kael'thas", "Chromie", "Li-Ming", "Kel'Thuzad",
          "Tracer", "Nazeebo", "Greymane", "Valla", "Cassia", "Lunara", "Zul'jin", "Falstad", "Gul'dan",
          "Raynor", "Tychus", "Genji", "Gall", "Azmodan", "Zagara", "Sgt. Hammer", "Sylvanas", "Probius",
          "Ana", "Junkrat", "Alexstrasza", "Hanzo", "Blaze", "Fenix", "Whitemane", "Mephisto"]


FRANCHISES = {
  "warcraft": ["Rexxar", "Anub'arak", "E.T.C.", "Stitches", "Muradin", "Garrosh", "Cho",
    "Arthas", "Chen", "Varian", "Rehgar", "Uther", "Li Li", "Malfurion", "Brightwing",
    "Tyrande", "Medivh", "Samuro", "Valeera", "Jaina", "Kael'thas", "Chromie", "Kel'Thuzad",
    "Greymane", "Ragnaros", "Illidan", "Lunara", "Zul'jin", "Falstad", "Gul'dan", "Thrall",
    "Gall", "Gazlowe", "Sylvanas", "Murky", "Alexstrasza", "Maiev", "Yrel", "Whitemane"],
  "starcraft": ["Artanis", "Dehaka", "Stukov", "Lt. Morales", "Tassadar", "Kerrigan",
    "Alarak", "Nova", "Zeratul", "Raynor", "Zagara", "Sgt. Hammer", "Probius", "Abathur",
    "Blaze", "Fenix"],
  "diablo": ["Diablo", "Johanna", "Sonya",  "Leoric", "Tyrael", "Kharazim", "Auriel",
    "The Butcher", "Li-Ming", "Malthael", "Nazeebo", "Valla", "Cassia", "Azmodan",
    "Deckard", "Mephisto"],
  "overwatch": ["D.Va", "Zarya", "Lucio", "Genji", "Tracer", "Ana", "Junkrat", "Hanzo",],
  "classic": ["The Lost Vikings"]
}

  
def get_by_id(hero_id):
  return filter(lambda hero: hero.hero_id == hero_id, HEROES)[0]
