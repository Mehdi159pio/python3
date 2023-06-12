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
print("la variable number1 est plus grnde que number2")

# elif == else if
# block if4
# réécriture du block if3 des if imbriqués
if number1 < number2:
   print("variable number1 est plus petite que number 2")
#else:
 #if number1 > number2:
      

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

# table de vérité de l'opérateur ou logique
#A     B      A and B
#True  True    True
#True   False   True
#False   True   True
#False   False   Flase





