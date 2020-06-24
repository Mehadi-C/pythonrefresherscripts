#!/bin/python3

#Importing
print("Importing is Important: ")

import sys #system functions and parameters 

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())

def newline():
	print('\n')

newline()

#Advanced Strings
print("Advanced Strings:")
myname= "Heatchcliffe"
print(myname[0]) #first initial
print(myname[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4])#first word
print(sentence[-9:-1])#last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split= sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

print('\n'.join(sentence_split))

quoteception = "'Mo Money'"
print(quoteception)

quoteception= "I said, \"Mo Money\""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Applie"

print(letter.lower() in word.lower())

too_much_space= "               hello                "
print(too_much_space.strip())

name= "Pikachu vs Darkrai"
print(name.replace("vs", "battling"))

print(name.find("Darkrai"))

movie="Hello"
print("This means {}". format(movie))

def favourite_book(title, author):
	fav= "My favourite book is \"{}\", which is written by {}.".format(title, author)
	return fav

print(favourite_book("Hello", "Aloha"))

newline()

#Dictionaries
print("Dictionaries are keys and values:")
drinks= {"ZERO": 7, "Again" : 10, "Lemon": 8, "Blueberry": 9} #string is key, price is value

print(drinks)

employees = {"Finance": ["Bob", "Linda"], "IT": ["Gene", "Ahmed"], "HR": ["MD", "YOLO"]}

print(employees)

employees['Legal']= ["Hello"] #add new key: value pair
print(employees)

employees.update({"Sales": ["And", "Or"]})
print(employees)

drinks["Yes"] = 10
print(drinks)

print(drinks.get("Yes"))
print(drinks.get("ZERO"))
print(drinks.get("1"))
print(drinks["Again"])

newline()

#Lists and Dictionaries
movies= ["When", "Hello", "Again"]
person = ["Heathcliffe", "Kirito", "Zoro"]
combined= zip(movies, person)
movie_dictionary= {key: value for key, value in combined}

print(movie_dictionary)




