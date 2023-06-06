#nombre entier
number1=123
numerber1=42
print(number1)

#nombre à virgule
number2=3.14
number=2.71
print(number2)

#chaine de caractère texte
text1='foo bar'
print(text1)
text2="foo bar bis"
print(text2)

#Boolean
python_is_cool=True
print(python_is_cool)


python_is_boring=False
print(python_is_boring)

#Valeur Null 
user_accepted_terms=None
print(None)

# Type de donnés
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

# Vérification du type de donnés
print(type(number1)is int)
print(type(number1) is str)

#todo: interroger le type des autres variables

#transtypage = type cating int>str
print(type(str(number1)))
print(str(number1))

#transtypage int>boolean
print(type(bool(number1)))
print(bool(number1))

number3=0
print(bool(number3))

#transtypage str>int
#print(type(int(text1)))

#il ne peut pas y avoir autre chose qu'un nombre
#dans la chaine de caractères
#si on veut la convertir int
text3= '123456789'
print(type(int(text3)))

# les fonctions de transtypage
#str() converti vers string
#int() convertie vers integer
#float() convertie vers float
#bool() convertie vers boolean

#chaine de caractèrès, strings
#
text4 = """<div>
       <h1></h1>
       </div>
       """     
print(text4)

#/n est équivalent à un saut de ligne 
#/t est équivalent à une tabulation 
text5="<div>/n/t<h1> Titre de premier niveau </h1>/n</div>\n"
print(text5)
#le backslash seul est le caractère
#\"est équivalent à une guillemet"
#\\est équivalent à un back slash \
text6= "Foo \"Bar \" Baz"
print(text6)

text7= "C:\\program Files\\Foo"
print(text7)

# permuter les deux variables a et b en utilisantl'opérateur d'affection et le nom des variables.
a=123
b=42

print(a)
print(b)







