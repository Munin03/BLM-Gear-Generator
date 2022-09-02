#constants/formulas last updated as of Sep. 1/2022, no main stat formula so evaluates purely based on substats.

from os.path import exists
import math
import csv
import damagecalcs

def write_csv(fname):
  global written
  if exists(fname) and written == False:
    with open(fname,'w',newline= '') as file:
      writer=csv.writer(file,'excel')
      writer.writerow(item_list)
      written = True
  else:
    with open(fname,'a',newline= '') as file:
      writer=csv.writer(file,'excel')
      writer.writerow(item_list)
def read_csv(fname):
  with open(fname,mode='r',buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as f:
    lname = [x for line in f for (x) in [line.strip().split(',')]]
  return lname

weapon= read_csv('6.2_weapons.csv')
head = read_csv('6.2_Head.csv')
body = read_csv('6.2_Body.csv')
hands = read_csv('6.2_Hands.csv')
legs = read_csv('6.2_Legs.csv')
feet = read_csv('6.2_Feet.csv')
earrings = read_csv('6.2_Earrings.csv')
necklace = read_csv('6.2_Necklace.csv')
bracelet = read_csv('6.2_Bracelet.csv')
ring1=read_csv('6.2_Ring.csv')

def increase(number1,number2,number3):
  if number1>=number2-1:
    number1 = 0
    number3 = number3+1
  return number1, number3

def materia(item_list):
  output_list =[]
  for n in range(len(item_list)):
    duck = item_list[n]
    name_int = duck[:2]
    stats = duck[2:]
    h_stat = int(max(stats))
    for i,val in enumerate(stats):
      val=int(val)
      stat = val
      stat=int(stat)+72
      if stat>h_stat:
        stat=h_stat
      newbugs=stats.copy()
      newbugs[i] = stat
      output_list.append(name_int+newbugs)
      newbugs.clear()
    for i,val in enumerate(stats):
      val = int(val)
      stat1 = val
      stat1=int(stat1)+36
      if stat1>h_stat:
        stat1=h_stat
      newbugs=stats.copy()
      newbugs[i] = stat1
      if i+1 < len(stats):
        stat2 = int(stats[i+1])
        stat2=stat2+36
        if stat2>h_stat:
          stat2=h_stat
        newbugs[i+1] = stat2
      else:
        stat2 = int(stats[0])
        stat2=stat2+36
        if stat2>h_stat:
          stat2=h_stat
        newbugs[0] = stat2
      output_list.append(name_int+newbugs)
      newbugs.clear()
  return output_list

weapon=materia(weapon)
head=materia(head)
body=materia(body)
hands=materia(hands)
legs=materia(legs)
feet=materia(feet)
earrings=materia(earrings)
necklace=materia(necklace)
bracelet=materia(bracelet)
ring1=materia(ring1)
ring2=ring1

r=len(ring2)
sets=0
written=bool(0)
a=b=c=d=e=f=g=h=i=j=k=z=0
highest = 0
while j < r:
  item_list = []
  weapo=weapon[z]
  hea=head[a]
  bod=body[b]
  hand=hands[c]
  leg=legs[d]
  fee=feet[e]
  earring=earrings[f]
  necklac=necklace[g]
  bracele=bracelet[h]
  rin1=ring1[i]
  rin2=ring2[j]
  for n in range(len(hea)):
    if n == 0:
      item_list.append(weapo[n])
      item_list.append(hea[n])
      item_list.append(bod[n])
      item_list.append(hand[n])
      item_list.append(leg[n])
      item_list.append(fee[n])
      item_list.append(earring[n])
      item_list.append(bracele[n])
      item_list.append(rin1[n])
      item_list.append(rin2[n])
      continue
    else:
      item_list.append(int(weapo[n])+int(hea[n])+int(bod[n])+int(hand[n])+int(leg[n])+int(fee[n])+int(earring[n])+int(bracele[n])+int(rin1[n])+int(rin2[n]))

  a=a+1
  a,b=increase(a,len(head),b)
  b,c=increase(b,len(body),c)
  c,d=increase(c,len(hands),d)
  d,e=increase(d,len(legs),e)
  e,f=increase(e,len(feet),f)
  f,g=increase(f,len(earrings),g)
  g,h=increase(g,len(necklace),h)
  h,i=increase(h,len(bracelet),i)
  i,j=increase(i,len(ring1),j)
  sets=sets+1
  if sets%500==0:
    print(sets,"...")

  #item_list[10] is intel
  #item_list[11] is dh
  #item_list[12] is crit
  #item_list[13] is det
  #item_list[14] is sps

  damage_sim = damagecalcs.damagecalcs(item_list[10],item_list[11],item_list[12],item_list[13],item_list[14])
  item_list.append(damage_sim)
  if highest == 0:
    print(damage_sim)
    highest = damage_sim
    print(highest)
    write_csv('6.2_sets.csv')
    print("First set!")
  if damage_sim>highest:
    highest=damage_sim
    write_csv('6.2_sets.csv')
    print("New best!")

print("Program complete\n")
print(sets,"sets generated")