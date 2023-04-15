#!/bin/python3

#PYTHON REFRESHER

def newline():
	print('\n')
newline()
#STRINGS
#--------
#Print string
print("Hello, world!")
print('Hello, world!') #single quotes are ok too
print("""This string 
runs multiple lines!""") #triple quotes for multi-line
print("This string is "+"awesome!") #you can concatenate strings
print('\n') #(\n) for new line

print("New line test")

newline()

#MATH
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print (50 / 50) #divide
print(50 + 50 - (50 / 50) * 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 / 6) #division with remainder (float)
print(50 // 6) #division with no remainder

newline()

#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #length of string/variable

name = "Sean"
age = 30

print(f"My name is {name} and I am {age} years old.")

newline()

#FUNCTIONS
def who_am_i(): #function without parameter
	name = "Sean"
	age = 30
	print(f"My name is {name} and I am {age} years old.")

who_am_i()

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

def add_two(x,y):
	print(x + y)

add_two(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

newline()

print("Je parle un peu le francais! Merci beaucoup.")

newline()
#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)

bool5 = "True"
print(type(bool5))

newline()

#RELATIONAL and BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_not = not True #False

for x in range(5):
	print("SKRILLEX G")

newline()

#CONDITIONAL STATEMENTS

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you bucko!"

print(drink(3))
print(drink(1))

newline()

def alcohol(age,money):
	if age >=21 and money >= 5:
		return "Drinks back on the menu boys!"
	elif age >=21 and money < 5:
		return "Bring back some mo cash buddy."
	elif age <=21 and money >= 5:
		return "Nice try kid."
	else:
		return "You're too young and too poor. Sadface emoji :("

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

newline()

#LISTS - Have brackets []

movies = ["The Matrix", "Kill Bill", "La La Land", "The Social Network", "The Girl with the Dragon Tattoo"]

print(movies[2]) #lists always start at 0
print(movies[0])
print(movies[1:4]) #return first index number up UNTIL the second value (but doesn't include it)

print(movies[:]) #prints all in a list
print(len(movies)) #prints number of items in list

movies.append("Eyes Wide Shut")
movies.insert(2, 'Watchmen')
print(movies)

movies.pop() #removes last item in a list
print(movies)

other_movies = ['Fight Club', 'Parasite']
dope_movies = movies + other_movies
print(dope_movies)

grades = [['Bob', 82], ['Alice', 90], ['Jeff', 73]]
alice_grade = grades[1][1]
print(alice_grade)

newline()

#TUPLES - Do not change, gets parentheses ()
num = ('1', '2', '3')

print(num[1])

newline()

#LOOPING
#While Loops - Execute as long as True (bool)

i = 1 
while i < 10:
	print(i)
	i += 1
	
newline()

#ADVANCED STRINGS
name = 'dotxdaemon'

print(name[0])
print(name[-1])

sentence = 'This is a sentence.'
print(sentence[:7]) #index number is CHARACTERS
print(sentence.split()) #delimiter - default in Python is a space

sent_split = sentence.split()
sent_join = ' '.join(sent_split) #define delimiter before .join(*variable*)

print(sent_join)

quote = "He said, \"give me all your money\""
print(quote)

too_many_zs = " zzzzzzzzzzzzzzzzzzz hello zzzzzzzzzzzzzzzzzzzzzzzzzzzz "
z = ' z'
print(too_many_zs.strip(z))

print('A' in 'Apple') #True

letter = 'A'
word = 'Apple'
print(letter.upper() in word.lower()) #False

movie = ['The Matrix', 'La La Land']
print(f'{movie[1]} is really cool.') #you can put list indices in an f-string. Neat.

newline()

#DICTIONARIES - key/value pairs {}

drinks = {'White Russian': 7, 'Old Fashioned': 10, 'Lemon Drop': 8} #drink is the key, price is the value

drinks['Muay Thai'] = 9
drinks.update({'Stella Artois': 6})
print(drinks)

print(drinks.get('Stella Artois'))

#END
# YOU DID IT. You're the man :)
