from os.path import exists
import csv

def read_csv(fname):
  with open(fname,mode='r',buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as f:
    lname = [x for line in f for (x) in [line.strip().split(',')]]
  return lname

head = read_csv('6.2_Head.csv')
body = read_csv('6.2_Body.csv')
hands = read_csv('6.2_Hands.csv')
legs = read_csv('6.2_Legs.csv')
feet = read_csv('6.2_Feet.csv')
earrings = read_csv('6.2_Earrings')
necklace = read_csv('6.2_Necklace.csv')
bracelet = read_csv('6.2_Bracelt.csv')
ring1=read_csv('6.2_Ring.csv')

def increase(number1,number2,number3):
  if number1>=number2-1:
    number1 = 0
    number3 = number3+1
  return number1, number3

x=y=z=0
r=len(body)
written = False

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

sets=0
while z < r:
  brain = head[x]
  bod = body[z]
  potato = necklace[y]
  
  for n in range(len(brain)):
    if n==0:
      item_set = []
      item_set.append(brain[0])
      item_set.append(neck[0])
      item_set.append(bod[0])
      continue
    item_set.append(int(brain[n])+int(neck[n])+int(bod[n]))

  if exists('6.2_sets.csv') and written == False:
    with open("6.2_sets.csv",'w',newline= '') as f:
      writer=csv.writer(f,'excel')
      writer.writerow(item_set)
      written = True
  else:
    with open("6.2_sets.csv",'a',newline= '') as f:
      writer=csv.writer(f,'excel')
      writer.writerow(item_set)

  x=x+1
  x,y=increase(x,len(head),y)
  y,z=increase(y,len(necklace),z)
  sets=sets+1

print("Program complete\n")
print(sets,"sets generated")