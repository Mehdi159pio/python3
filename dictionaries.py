fruits = {  
    'a': 'ananas',
    'b':'banane', 
    'c': 'cerise',
}

print(fruits)
# accès en lecture
print(fruits['a'])
fruit = fruits ['a']

# accès en écriture
fruits ['a'] = 'abricot'

print(fruits)

#boucle foreach pour obtenir les clés
for key in fruits:
    print(f"{key=}")
    print(fruit[key])
    # fruits [key] contient la valeur associée à la clé
    print(f"fruit ={fruits[key]}")
# boucle foreach pour obtenir les clés et les valeurs en mme temps
for key , value in fruits.items():
    print(f"{key = }")
    print(f"{value = }")
# boucle foreach pour obtenir les valeurs seuleument
for value in fruits.values():
    print(f"{value =}")
#dictonnaire avec clés de tout type
my_dict = {
       100:'foo',
       3.14:True,
       True: 'abc',
       None: 123,
}
