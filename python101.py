#!/bin/python3

#Print String

print("Strings and things:")
print('Hello, World!')
print("""Hello, this is
a multi-line string!""")

print("This is" + " a string")

print('\n') #new line

#Math
print("Math time:")
print(100 + 100)#add
print(100 - 100)#subtract
print(100*100)#multiply
print(100/100)#divide
print(100 + 100 - 100 *100/100)#BEDMAS
print(100 ** 2)#exponents
print(100 % 9)#Modulo
print(100//6)#number without leftovers (just the enter, with no floats or decimals)

print('\n') #new line

#Variables & Methods
print("Fun with variables and methods:")
quote= "SOUP"
print(len(quote)) #length of characters
print(quote.upper()) #upper case
print(quote.lower()) #lower case
print(quote.title()) #title

print('\n') #new line

name="Heathcliffe"
age= 27 #int int(27)
gpa= 3.99 #float float(3.99)

print(int(age))
print(int(27.7))#does not round -- takes the floor

print("My name is " + name + " and I am " + str(age) + " years old.")#cant use multiple types, so we are using str(the int value)

print('\n') #new line

#functions
print("Now, some functions:")
def who_am_i():
	name1="heathcliffe"
	age1= 27
	print("My name is " + name1 + " and I am " + str(age1) + " years old.")

who_am_i();

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(200);


#add in multiple parameters
def add(x, y):
	print(x + y)

add(777, 777)


#using return
def multiply(x, y):
	return x*y

print(multiply(100, 100))


def square_root(x):
	return x**.5

print(square_root(64))

print('\n') #new line

#boolean expressions (True or False)
print("Boolean expressions:")
bool1= True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

print('\n') #new line

#relational and boolean operators
greater_than= 7 > 5
less_than= 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to= 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and= (7 > 5) and (5 < 7)
test_or= (7 > 5) or (5 < 7)
test_not = not True

print(test_and, test_or, test_not)

print('\n') #new line

#conditional Statements
print("Conditional Statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "Not enough to buy a soda!"

print(soda(100))
print(soda(1))

def bev(money, age):
	if (money >= 5) and (age >=21):
		return "Purchase Completed"
	elif (age >= 21) and (money < 5):
		return "Not enough to purchase"
	else:
		return "Too young"
		
print(bev(50, 25))
print(bev(3, 25))
print(bev(5, 19))

print('\n') #new line

#lists
print("Lists have brackets:")
movies = ["When", "The", "LOL", "AWESOME"]

print(movies[1])
print(movies[1:3])

print(movies[1:])

print(movies[:2])

print(movies[-1])#pulls the last item on the list
print(len(movies))

movies.append("Yes")
print(movies)

movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["When", "The", "LOL", "AWESOME"]
person= ["Me", "Jake", "Hello", "Hi"]
combined = zip(movies, person)
print(list(combined))

person.pop()
combined= zip(movies, person)
print(list(combined))#because one of the arrays is shorter, the fourth index disappears in the combined

print('\n') #new line

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
print("For Loops - start to finish iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

print("While Loops - Execute as long as True:")
i= 1
while i <= 10:
	print(i)
	i += 1
	




