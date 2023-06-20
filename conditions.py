import random
if True:
 print("Ce message s'affiche toujours")

if False:
    print("Ce message ne s'affiche jamais")
number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(f'{number1 =}')
print(f'{number2 =}')

if number1 < number2:
  print("La variable number1 est plus petite que number2")
else:# number1 >= number2
   print("les deux variable number1 et number2 sont égales")

# elif number1 > number 2
print("la variable number1 est plus grande que number2")

# elif == else if
# block if4
# réécriture du block if3 des if imbriqués
if number1 < number2:
   print("variable number1 est plus petite que number 2")
#else:
# if number1 > number2:

 
# opérateurs booléens
# négation
# print(not True)
# print(not False)

# table de vérité de l'opérateur de négation
# A    not A
# True False
# False True

# ou logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# table de vérité de l'opérateur ou logique
#A     B      A or B
#True  True    True
#True   False   True
#False   True   True
#False   False   Flase



# ET logiqueprint(True or True)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# table de vérité de l'opérateur ET logique
#A     B      A and B
#True  True    True
#True   False   True
#False   True   True
#False   False   Flase

# table de vérité de l'opérateur NAND (not and)
#A     B      A and B     not (A and B)
#True  True    True       False
#True   False   True      True
#False   True   True      True
#False   False   Flase    True

# OU EXCLUSIF

print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

#A     B       A XOR B      
#True  True     False     
#True   False   True      
#False   True   True      
#False   False   Flase  

# exo  course (opérateur OU logique)
has_cash = bool(random.randint(0,1))
has_cb = bool(random.randint(0,1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash or has_cb :
 print("le moyen de payement ")

else:
 print("aucun moyen de payement")

 # exo courses (opérateur ET Logique)
 # remplissez le meme cahier des charges mais avec l'opérateur ET
 
if not has_cash == False and not has_cb ==False:
  print("le moyen de payement")

else:
 print("aucun moyen de payement")


# combinaison d'opérateur AND et OR
 
 user_level = 3
 user_xp = 90
 user_credit = 0 

 if user_level >3 and user_xp >= 100 or user_credit >=100:
   print("le joueur peut acheter du matériel")
 else:
   print("le joueur ne peut pas acheter de matériel")

# exo carte de réduction
# déterminé la carte de réduction auquelle le voyageur à droit :
# entre 0 et 11 (inclus) , le voyageur droit à la gratuité
# entre 12 et 25 ans (inclus) , le voyageur a droit à une réduction de 50%
# entre 26 et 64 ans (inclus) , le voyageur a droit à une réduction de 10%
# au de la de 65 ans (inclus) , le voyageur a droit à une réduction de 50 %

 age= random.randint(0, 99)

if age >= 0 and age <=11:
  print(" gratuieté")

elif age >=12 and age >=25:
  print("reduction 50%")
elif age >=26 and age <=64:
  print("reduction 10%")
elif age >=65 and age <=99:
  print("réduction 50%")

  





