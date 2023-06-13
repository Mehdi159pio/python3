text1 = "lorem"
text2 = 'ipseum'
# concaténation
text3 = text1+" "+ text2
print(text3)


# interpolation avec une f -string
text3 = f" {text1} {text2}"
print(text3)
# attention : la concaténantion ne fonctionne qu'avec des str
# solution : convertir les atres types en str
mails = 52
text4 = "vouss avez" +str(mails ) + " non lus "
print(text4)

# répétition de texte
text5 = "foo"*3
print(text5)

# affichage de valeurs arrondies
number1 = 10 / 3
text6 = f"10 / 3 est à peu prés égal {number1:.2f}"
print(text6)

# les fonctions associés aux string 
text7= "abc"
print(len(text7))
#compter des mots
print(text7.count('foo'))
# retrouvre l'emplacement d'un mot
position = text7.find('foo')
print(position)
#pour trouver l'occurence suivante , il faut chercher une position plus loin

print(text7.find('foo', position+ 1))

# si le mot est absent , la fonction renveoie -1
position = text7.find('lorem')
print(position)

# remplacement de mots
texte7 = text7.replace('foo','lorem')
print(text7)

# split et join
list1 = text7.split(' ')
print(list1)


text8 = "+". join(list1)
print(text8)
