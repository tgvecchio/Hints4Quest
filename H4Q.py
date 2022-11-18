import random
import uuid
import csv
import os
import urllib

def support_files():
    cwd = os.getcwd()
    print ('Working directory', cwd)
    cd = os.path.dirname(os.path.abspath(__file__))
    print('Current directory',cd)
    print()
    print('Reading lists')

    global casa_tel
    global arch
    global race
    global myth
    global spell
    global prep
    global trink
    global tempv
    global weapon
    global place
    global failure
    global noun
    global orientation_a
    global orientation_b
    global kunderas_personae_PLURALITY
    global kunderas_personae_PERSONIFICATION
    global kunderas_personae_HISTORY
    global kunderas_personae_COMMUNICATION
    global direction
    global conflict_type
    global conflict_type2
    global symbols
    global weapondnd
    global damage_status
    global Round_nr

    casa_tel = [line.strip() for line in (line.rstrip('\n') for line in open(cd + "/" + "00casa_tel.txt")) if line.strip() != '']
    arch = [line.rstrip('\n') for line in open(cd + "/" + "00archetypes.txt")   if line.strip() != '']
    race=[line.rstrip('\n') for line in open(cd + "/" + "00races.txt")  if line.strip() != '']
    myth =  [line.rstrip('\n') for line in open( cd + "/" + "00Myth_creatures.txt") if line.strip() != '' ]
    spell = [line.rstrip('\n') for line in open(cd + "/" + "spells.txt")  if line.strip() != '']
    prep =   [line.rstrip('\n') for line in open(cd + "/" + "prepositions.txt") if line.strip() != '' ]
    trink =   [line.rstrip('\n') for line in open( cd + "/" + "trinkets.txt")  if line.strip() != '']
    tempv =   [line.rstrip('\n') for line in open(cd + "/" + "tempverb.txt")  if line.strip() != '']
    weapon =   [line.rstrip('\n') for line in open(cd + "/" + "weapon.txt") if line.strip() != '']
    place =   [line.rstrip('\n') for line in open(cd + "/" + "places.txt") if line.strip() != '']
    failure=[line.rstrip('\n') for line in open(cd + "/" + "consequence.txt") if line.strip() != '']
    noun=[line.rstrip('\n') for line in open(cd + "/" + "nounlist.txt") if line.strip() != '']

    orientation_a =['Evil', 'Good', 'Neutral']
    orientation_b =['Chaos', 'Lawfull', 'Neutral']

    kunderas_personae_PLURALITY = ['Singular', 'Outsider','Cloned','By others','False unity','Trviality']
    kunderas_personae_PERSONIFICATION = ['Soul','Face', 'Body', 'Corpse']
    kunderas_personae_HISTORY = ['Awarness','Agnostic','Idyll','Utter destitution']
    kunderas_personae_COMMUNICATION = ['Missinterpretation','Graphomaniac','Truthfull','Silent']

    direction=['N', 'NE','E','SE','S','SW','W','NW']
    conflict_type=['Man', 'Society','Nature', 'Technology','Fate']
    conflict_type2=['Man', 'Self', 'Society','Nature', 'Technology','Fate']
    symbols=['PROTECT', 'ATTACK', 'BUILD', 'DESTROY', 'HEAL', 'KILL', 'FIND', 'HIDE']
    weapondnd = ['Crossbow Light', 'Dart', 'Shortbow', 'Sling', 'Blowgun', 'Crossbow hand', 'Crossbow Heavy', 'Longbow', 'Net', 'Club','Dagger','Greatclub','Handaxe','Javelin','Light hammer','Mace','Quarterstaff','Sickle','Spear','Unarmed Strike', 'Battleaxe','Flail','Glaive','Greataxe','Greatsword','Halberd','Lance','Longsword','Maul','Morningstar','Pike','Rapier','Scimitar','Shortsword','Trident','War pick','Warhammer','Whip']
    damage_status = ['Pathetic', 'Bad', 'Medium', 'Good', 'Excellent','Superior']
    Round_nr = int()

def create_values():
  canvas = 'clear'
  os.system(canvas)
  Dmg = random.choice(damage_status)
  Weapondnd=random.choice(weapondnd)
  Race=random.choice(race)
  Noun=random.choice(noun)
  Faliure=random.choice(failure)
  Symbol=random.choice(symbols)
  Place=random.choice(place)
  Conf2=random.choice(conflict_type2)
  Conf=random.choice(conflict_type)
  Weapon=random.choice(weapon)
  Verb=random.choice(tempv)
  Trink=random.choice(trink)
  Prep=random.choice(prep)
  Spell=random.choice(spell)
  Myth=random.choice(myth)
  Direction=random.choice(direction)
  Orientation=random.choice(orientation_b)+'-'+random.choice(orientation_a)
  Arch=random.choice(arch)
  D100=round(random.randrange(1,101))
  D20=round(random.randrange(1,21))
  D10=round(random.randrange(1,11))
  Act_pot=round(random.gauss(5,2))
  UID=uuid.uuid4()
  Casa_tel=random.choice(casa_tel)
  yes_25 = reset(25)
  yes_50 = reset()
  yes_75 = reset(75)
  
  
  global Round_nr
  if Round_nr > 0:
    Round_nr = Round_nr + 1
    print('--------®')
    print('Round:',Round_nr)
  else:
    Round_nr = 1
    print('--------®')
    print('Round:',Round_nr)
  
  return (Dmg, Weapondnd, Trink, Race, Faliure, Noun, Symbol, Place, Conf2, Conf, Weapon, Verb, Prep, Spell, Myth, D100, D10 ,Direction, Orientation, Arch, D20, Act_pot, UID, Casa_tel, yes_25, yes_50, yes_75)


def new_card():
  deck_of_hints = create_values()
  #print(deck_of_hints)
  with open("Deck_of_Hints.csv", "a") as fp:
    wr = csv.writer(fp)
    wr.writerow(deck_of_hints)
  with open("Deck_of_Hints.csv", "r") as db:
    print('--------✓')
    print("New card:")
    Your_card= ', '.join(reversed(list(csv.reader(db))[-1])) 
    #print(Your_card)
  return Your_card
 
 
def draw_from_discard_pile():
  canvas = 'clear'
  os.system(canvas)
  with open("Deck_of_Hints.csv", "r") as db2:
    print('------------')
    print('DISCARD PILE')
    print('---------✓')
    print("Last card:")
    Your_discard =  ', '.join(reversed(list(csv.reader(db2))[-2]))
  return Your_discard


def iterator():
  canvas = 'clear'
  os.system(canvas)
  with open("Deck_of_Hints.csv", "r") as db2:
    print('------------')
    print('DISCARD PILE')
    print('---------✓')
    
    Your_discards =  list(csv.reader(db2))[::-1]
    for i in Your_discards:
        i=', '.join(reversed(i))
        print('See previous card? y/n')
        valor=input()
        if 'y' in valor:
          #print(i)
          design_card(i)
        else:
          canvas = 'clear'
          os.system(canvas)
          break
    
  return
    

def iterate_discarded(): ####NOT IN USE
  with open("Deck_of_Hints.csv", "r") as db3:
    discarded = csv.reader(db3)
    for row in list(discarded)[::-1]:
        print('Continue?')
        valor=input()
        if 'y' in valor:
            print(row)
        else:
            break
    #print(list(discarded)[::-1])
    #Your_card= (reversed(list(csv.reader(db3)))) 
    #print(Your_card)
    
    
def round_cournter():###NOT IN USE###
      global Round_nr
    
      if Round_nr > 0:
        Round_nr = Round_nr + 1
        print('------------')
        print('Round:',Round_nr)
        print('------------')
      else:
        Round_nr = 1
        print('------------')
        print('Round:',Round_nr)
        print('------------')

     
def reset(percent=50):
    return random.randrange(100) < percent


def design_card(a):
    parts = a.split(',')
    aa,bb,cc,dd,ee,ff,d20,hh,ori,direc,d10,d100, crea, spe, prepo, ver, wea, confl, confl2, pla, sym, nou, fail, rac, trin, wdnd, dmg= parts
    ff =int(ff)
    if Round_nr > ff:
        alert = 'Narrative turn! Chose random encounter or action'
    else:
        alert = ' '
    
    print('D100', d100, '||', 'D20', d20, '||', 'D10', d10, '||', direc, '✓')   
    print('Action Potential:', ff, alert, '|∆|' , sym)
    #print()
    #print('ODDS: low', cc, '|', 'norm', bb,'|','high',aa)
    print('|    Low odds:', cc)
    print('||       Odds:', bb)
    print('||| High Odds:', aa)
    print()
    print('Name:    ', dd, '||', 'phonetic')
    print('Creature:', rac,'||',crea)
    print('Weapon/tool:', wdnd,'||', wea)
    print('Status:', dmg)
    print()
    print('Orientation:', ori)
    print('Magic:', spe)
    print('Virtue | Flaw')
    print()
    print('<<Archetype>>', hh)
    print()
    print('-_-NARRATIVE ARC-_-')
    print('| Inciting Incident:')
    #print()
    print('|| Conflict type:', confl, ' vs ', confl2)
    #print()
    print('||| Consequence:', fail)
    print()
    print('| Location:', pla)
    #print('An event:')
    print('|| Event', ver, ' ', prepo, ' ', nou)
    print()
    print('|',trin)
    #print()
    ee=ee[:19]
    print('|| Card UUID:', ee)


def main():
  canvas = 'clear'

  print ('#######################')
  print ('Welcome to Hints 4 Quest')
  print ('#######################')

  support_files()
  
  while True:
    #print('------------------?')
    print ('Get new card:  y/n'); val=input();
    if 'y' in val:
      design_card(new_card())
    else:
      #design_card(draw_from_discard_pile())
      iterator()


  
if __name__ == "__main__":
  main()
  #print('END')
  #iterate_discarded()
  #iterator()


