import random
import os
import shutil


#AULA 16 - 2D Lists

# drinks = ["coke", "water", "soda"]
# dinner = ["chicken", "pasta", "beef"]
# deserts = ["ice cream", "cookie"]
# food = [drinks, dinner, deserts]

# print(f"""Our drinks are: {food[0]}
# Our main dinner are: {food[1]}
#  Our deserts are: {food[2]}""")


#AULA 17 - TUPLES


# student = ("Bro", 21, "male")

# print(student.count("Bro"))
# print(student.index(21))

# for x in student:   
#     print(x)

# if "Bro" in student:
#     print("Bro is here!")

#AULA 18 - SETS

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkins")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)

# dishes.difference(utensils)
# dishes.intersection(utensils)


# AULA 19 - DICIONARIOS 
# KEY : VALUE


# capitals = {'USA': 'Washington DC',
#             'India':'New Dehli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}

# capitals.update({"Germany":"Berlim"})
# capitals.update({"USA": "Las Vegas"})
# capitals.pop("China")
# capitals.clear()



# print(capitals['China']) #Perigoso!!!! Caso eu queira acessar uma chave nao existente, ele lança uma execao e para o programa
# print(capitals.get('Germany')) #Não lança erro, retorna NONE caso nao exista
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)

# AULA 20 - INDEXING

# name = 'pedro grigolli'

# if (name[0].islower()):
#     name = name.capitalize

# secondName = name[6:14]

# print(name)
# print(secondName.capitalize())


# AULA 26 - ARGS

# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    

# print(add(1,2,3,4,5,6,7))

# AULA 27 - KWARGS

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keywords arguments

# def hello(**kwargs):
#     print("Hello",end=' ')
#     for key,value in kwargs.items():
#         print(value, end=' ')

# hello(title = "Mr.", first = "Pedro", middle = "Chouery", last = "Grigolli")

#AULA 29 - RANDOM NUMBERS

# x = random.randint(1,6)
# y = random.random()

# myList = ["rock", "paper", "scissors"]
# z = random.choice(myList)

# cards = ["A",2,3,4,5,6,7,8,9,"J","Q","K"]
# random.shuffle(cards)

# print(x)
# print(y)
# print(z)
# print(cards)


#AULA 31 - FILE DETECTION

# path = "C:\\Users\\Usuario\\Desktop\\testePython.txt"

# if os.path.exists(path):
#     print("That location exists!!")
#     if os.path.isfile(path):
#         print("That is a file!!")
#     elif os.path.isdir(path):
#         print("That is a directory!!")
# else:
#     print("That location doesn't exists!!")


#AULA 32 - READ A FILE

# try:
#     with open("C:\\Users\\Usuario\\Desktop\\testePython.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found!")
# else:  
#     print("File found!")

# AULA 33 - WRITE A FILE **mesma coisa de C

# text = "OIEEEEE BOM DIA AAAA A A A  A"

# with open("C:\\Users\\Usuario\\Desktop\\testePython.txt","w") as file:
#     file.write(text)


#AULA 33 - COPY FILE

shutil.copy("C:\\Users\\Usuario\\Desktop\\testePython.txt","test.txt")

asdasdasdasd




























