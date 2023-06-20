import library

# definition
def hello():
    print('hello Python!')

# appel ou exécution 
hello()

def hello2 (name) :
    print (f"hello {name}!")

    hello2('foo')

def addition(a,b):
    return a+b
resultat = addition(42, 123)
print(resultat)
# appel d'une fonction stocké dans un autre module
Resultat= (library.oui_non(False))
print(resultat)
print(library.oui_non(True))

#reverse lookup
my_list = [ 42, 123, 3.14,]

def reverse_lookup(my_list, value):
# Cette fonction prenden parmètre une liste et une valeur à rechercher.
# elle renvoie l'index de la valeur si elle est trouvée, ou None si la valeur n'est pas trouvée.


#my_list la liste dans laquelle il fait chercher
# value any la valeur à chercher return int si la valeur ou None si la valeur n'est pas trouvé



  for i in range(len(my_list)):
    if my_list [i] == value:
     return i

reverse_lookup(my_list,123)
result = reverse_lookup(my_list,0)
print(result)