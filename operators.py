# import du module random (pour les nombres aléatoires)
import random

# aritmetique
a= 42 + 123
a= 42 - 123
a= 42 * 123
a= 42/ 123

# division entière, intéger division
a= 123 // 42
print(a)
# modulo ou reste de la division (euclidienne)
a=53
# s'il y a a un rste, le nombre n'est pas divisible par deux , donc il n'est pas pair
print(a%2)
a= 74
#s'il y a un reste , le nombre n'est pas divisible par deux , donc il n'est pas pair
print(a%2)
#puissance , exponentiation
#deux puissance trois
a= 2 ** 3
print(a)

#opérateur de comparaison
print(123 == 123)
 #operateur d'égalité
result=123 ==42
print(result)
password="abc"
user_input= "def"
print(password==user_input)
 # plus grand que
print(123 > 42)
#plus grand ou égal à
print(42>=42)
 # plus petit que 
print(123<42)
#plus petit ou égal
print(42!=42)

# opérateurs composés
b = 0

# incrémentation
# b= b +1
b += 1
b += 1
print(b)

# déccrémentation
# b= b -1
b -= 1
print(b)

# mutiplication
c= 3
# c = c * 2
c *= 2
print(c)

# division
d=10
# d = d / 3
d /= 3
print(d)

# division entière
d=10
#d = d// 3
d //= 3
print(d)

# opérateur d'inclusion
text1= "Lorem ipsum"
result = "e" in text1
print(result)
print("e" in text1)
print ("Lorem" in text1)
print ("lorem" in text1)

list1 = ['Lorem', 'ipsum']
print( 'e' in list1)
print('ipsum' in list1)

# comparaison avec des nombres aléatoires
e = random.randint(0 , 100)
f = random.randint(0 , 100)

print(f'{e = }')
print(f'{f = }')

ressult = e  ==f
print(result)

result = e < f
print(result)

#exression
# 1 + 1 -> 2

#(100+2) *3 -> 102 *3 -> 306
# 1 + 1 > (100 + 2)*3 -> 306 -> False
# random.randint(0, 100) -> 100

# pas une expression
# print(100) ->








