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


# type hinting

def mult(a:int, b: int) -> int:
  #cette fonction ...a....b return
  
   return a*b


result = mult(2, 5)
print(result)


# le nom de la fonction + ses paramètres + sont type de retour = signature de la fonction
# def mult(a: int, b: int) -> int :

#le nom de la fonction + ses parmètres + sonttype de retour=signature de la fonction
#def mult(a:int,b:int)->int:
#copie d'une fonction comme si c'était une variable

mult_copy = mult
mult_copy(2,5)

# fonction de degré supérieur
# une fonction qui accepte une fonction en parmètre
# ou qui renvoi une fonction

def operateur_binaire(a,b,fonction):
    return fonction(a,b)

# appel de la fonction de degré supérieur
résultat = operateur_binaire(2,5,mult)

operation = [] 
operation.append(addition)
operation.append(mult)

a = 2
b = 5
resultat = None
for operation in operation :
    resultat = operation(a,b)
    print(resultat)

#
my_list = ['foo',"ipsum"]
text = "toto"

print(len(my_list))
print(len(text))

def my_len(value):
   return 42

# saugarde de le fonction len () originale
len_backup= len
#surchage de la fonction len originale
#c- a-d remplacement par une autre fonction
len = my_len

print(len(my_list))
print(len(text))

#restauration de la fonction len()originale

len = len_backup