myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))


"concatenação"
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

"strings de entrada"
name = input("Qual é o seu nome? ")
print(name)

"strings de saída"
color = input("Qual é a sua cor favorita? ")
animal = input("Qual é o seu animal favorito? ")
print("{}, você gosta da  {} {}!".format(name,animal,color))