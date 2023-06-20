
import random

#while : c'est comme  un "if" mais qui est répété
#while False :
print("ce message ne s'affiche pas")
#exit()

# crtl+c pour arréter le programme
# while True :
# continue permet de reprendre au début de la boucle suivante
#print("ce message est affiché en boucle")
# break prmet de sortir de la boucle
#break

# premeier tirage
dice=random.randint(1,6)

while dice!=6:
  print(f"Je n'ai pas tiré 6,mais un {dice}")
  print("Je recomnce un nouveau tirage")
  dice=random.randint(1,6)

else:
  print("Je n'ai pas tiré un 6")

# recréation de la boucle for classique avec une boucle while
i = 0 
while i < 10:
  print(f'{i=}')
  i += 1

  # boucle for classique en python
  # 0 est inclus mais 10 est exclu
  for i in range(0,10):
    print(f'{i =}')

  for i in range(10,0,-1):
    print(f'{i=}')
  # boucle for each imporant c'est la list 
  users = {'foo','bar','baz'}
  for user in users:
    print(user)
  #enumerate permet de récupérer l'index de chaque élément
  for i, user in enumerate(users):
       print(f"{i=}, {user=}")

# boucle for  basé sur l'index
 # for i in range(0, len(users)):
   # user = user[i]
   # print(f"{i=}, {user=}")

# accumulateur
accumulateur = 0
for i in range(1,11):
  accumulateur +=i
  print(f"{i=}")
  print(f"{accumulateur = }")

  print()
  print(f"{accumulateur =}")

# liste 20
players = [
  [14200,46400,32103],
  [16700,44667,57987],
]
line = 0
col= 0
print(players [line][col])

for line_index in range(0,len(players)):

  line = players(line_index)
  for col_index in range(0,len(line)):
    score = line[score]

# utiliser la valeur  dans une boucle
numbers = [123,42,1000,3.14]

for number in numbers:
  print(number)
