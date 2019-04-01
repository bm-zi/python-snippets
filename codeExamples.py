#!/usr/bin/env	python
# -*- coding: utf-8 -*-

# Author: bm-zi


import os

def f1():
	# Math Operators
	# --- CHAPTER 1 ---	
	print(2+2)	# 4
	print(2)	# 2     
	print(2 + 3 * 6)	# 20
	print((2 + 3) * 6)	# 30
	print(48565878 * 578453)	# 28093077826734
	print(2 ** 8)	# 256
	print(23 / 7)	# 3.2857142857142856
	print(23 // 7)	# 3
	print(23 % 7)	# 2
	print(2    +    2)	# 4
	print((5 - 1) * ((7 + 1) / (3 - 1)))  # 16.0
	print()  # blank line in python3


def f2():
	# String concatenation and replication
	print('Alice' + 'Bob') # AliceBob
	print('Alice' * 5)	# AliceAliceAliceAliceAlice


def f3():
	# First Python Program
	
	print('Hello world!')
	print('What is your name?') # ask for their name,
	                            # name has to be entered as a string like 'Jim' in python2
	myName = input()
	print('It is good to meet you, ' + myName)
	print('The length of your name is:')
	print(len(myName))
	print('What is your age?') # ask for their age
	myAge = input()
	print('You will be ' + str(int(myAge) + 1) + ' in a year.')


def f4():
	# Function len()
	print(len('hello'))
	print(len('My very energetic monster just scarfed nachos.'))

def f5():
	# Function str()
	print('I am ' + str(29) + ' years old.')  # you get an error if you just use 29 without functionstr()

def f6():
	# Function str(), int(), float
	# The str() , int() , and float() functions will evaluate to the string,
	# integer, and floating-point forms of the value you pass, respectively.
	print(str(0))     # 0
	print(str(-3.14)) # -3.14	
	print(int('42'))  # 42
	print(int('-99')) # -99
	print(int(1.25))  # 1
	print(int(1.99))  # 1
	print(float('3.14'))  # 3.14
	print(float(10))  # 10.0

def f7():
	# input() function
	# input() function always returns a string,
	# to change it to an integer use int() function
	spam = input()  
	spam = int(spam)
	print(spam)   # If you type a string that cannot be converted to integer,
	              # you will get an error shows that the variable is not defined
	              # These are error:  int('99.99') int('twelve')

	print(int(7.7))      # 7
	print(int(7.7) + 1)  # 8
	print(42 == '42')    # False
	print(42 == 42.0)	 # True
	print(42.0 == 0042.000)   # True
	print()	
	print()
	print()

def f8():
	# Boolean data types
	# --- CHAPTER 2 ---
	# Boolean data types are having values: False and True
	
	print(42 == 42)   # True
	print(42 == 99)   # False
	print(2 != 3)	  # True
	print(2 != 2)     # False 
	
	# The == and != operators can actually work with values of any data type.
	
	print('hello' == 'hello')   # True
	print('hello' == 'Hello')   # False
	print('dog' != 'cat')  		# True
	print(True == True)    		# True
	print(True != False)   		# True
	print(42 == 42.0)      		# True
	print(42 == '42')      		# False
	
	print(42 < 100)     	# True
	print(42 > 100)     	# False
	print(42 < 42)      	# False
	
	eggCount = 42
	print(eggCount <= 42)   # True
	
	myAge = 29
	print(myAge >= 10)      # True

def f9():
	# Boolean Operators
	# and operator
	print(True and True)   	# True
	print(True and False)	# False
	print(False and True)	# False
	print(False and False)	# False
	
	
	# or operator
	print(True or True)		# True
	print(True or False)	# True
	print(False or True)	# True
	print(False or False)	# False
	
	# not operator
	print(not True)		# False
	print(not False)	# True

def f10():
	# Mixing Boolean and Comparison Operators
	print((4 < 5) and (5 < 6))		# True
	print((4 < 5) and (9 < 6))		# False
	print((1 == 2) or (2 == 2))		# True
	print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)		# True


def f11():
	# if,elif,else conditional
	name='alice'
	age=20
	
	if name == 'Alice':
		print('Hi, Alice.')
	elif age < 12:
		print('You are not Alice, kiddo.')
	else:
		print('You are neither Alice nor a little kid.')


	spam = 0
	if spam < 5:
		print('Hello, world.')
		spam = spam + 1


def f12():
	# while loop
	spam = 0
	while spam < 5:
		print('Hello, world.')
		spam = spam + 1


def f13():
	# An Annoying while Loop
	name = 'Al'
	while name != 'your name':
		print('Please type your name.')
		name = input()
	print('Thank you!')


def f14():
	# break Statements
	while True:
		print('Please type your name.')
		name = input()
		if name == 'your name':
			break
	print('Thank you!')


def f15():
	# continue statement
	while True:
		print('Who are you?')
		name = input()
		if name != 'Joe':
			continue   # restart the loop      
		print('Hello, Joe. What is the password? (It is a fish.)')
		password = input()
		if password == 'swordfish':
			break	   # stops the loop
	print('Access granted.')


def f16():
	# empty value is considered False
	name = ''
	while not name:		
		print('Enter your name:')
		name = input()
	print('How many guests will you have?')
	numOfGuests = int(input())
	if numOfGuests:     # if no of guest not empty
		print('Be sure to have enough room for all your guests.')
	print('Done')


def f17():
	# for Loops and the range() Function
	print('My name is')
	for i in range(5):
		print('Jimmy Five Times (' + str(i) + ')')


def f18():
	# equivalent while loop
	print('My name is')
	i = 0
	while i < 5:
		print('Jimmy Five Times (' + str(i) + ')')
		i = i + 1


def f19():
	# Another for loop example - sum of numbers from 1 to 100
	total = 0
	for num in range(101):
		total = total + num
	print(total)



def f20():
	# range() function examples
	for i in range(12, 16):
		print(i)

	
	print('.' * 10)

	for i in range(0, 10, 2):
		print(i)

	print('.' * 10)	
	
	for i in range(5, -1, -1):
		print(i)



def f21():
	# import modules
	# functions like print(), input() , and len() are builtin fuctions. No need to import them.
	# function like randint() are from standard library modules that has to be imported

	# if use "from random from random import *" , 
	# then no need to to call a function with the random. prefix.

	import random
	for i in range(5):
		print(random.randint(1, 10))


def f22():
	# sys.exit()
	# Ending a Program Early with sys.exit()

	import sys
	while True:
		print('Type exit to exit.')
		response = input()
		if response == 'exit':
			sys.exit()
		print('You typed ' + response + '.')



def f23():
	# FUNCTIONS
	def hello():

		print('Howdy!')
		print('Howdy!!!')
		print('Hello there.')
	hello()
	hello()
	hello()


def f24():
	# Function with argument
	def hello(name):

		print('Hello ' + name)
	hello('Alice')
	hello('Bob')


def f25():
	# return statement
	import random
	def getAnswer(answerNumber):

		if answerNumber == 1:
			return 'It is certain'
		elif answerNumber == 2:
			return 'It is decidedly so'
		elif answerNumber == 3:
			return 'Yes'
		elif answerNumber == 4:
			return 'Reply hazy try again'
		elif answerNumber == 5:
			return 'Ask again later'
		elif answerNumber == 6:
			return 'Concentrate and ask again'
		elif answerNumber == 7:
			return 'My reply is no'
		elif answerNumber == 8:
			return 'Outlook not so good'
		elif answerNumber == 9:
			return 'Very doubtful'

	r = random.randint(1, 9)
	fortune = getAnswer(r)
	print(fortune)


def f26():
	# None
	# 'None' is a value-without-value (like null or undefined in other languages.)
	spam = print('Hello!') # prints returns no value that is known as 'None'
	print(None == spam)

	# return without value returns value 'None'
	# continue in for or while loop also returns value 'None'



def f27():
	# Optional keywords for functions
	# functions have optional keyword like end and sep in print() function
	
	print('Hello', end='')                 # The 'end' keyword cause to ignore the new line.
	print('World')	                       # By defualt print prints a newline after printing 
	                                       # its argument
	print('cats', 'dogs', 'mice')
	print('cats', 'dogs', 'mice', sep=',') # the function print will automatically 
										   # separates multiple string values
										   # with a single space.


def f28():
	# Local and Global Variables with the Same Name
	# you should avoid using the same variable name in different scopes.
	def spam():
		eggs = 'spam local'
		print(eggs)            # prints 'spam local'

	def bacon():
		eggs = 'bacon local'
		print(eggs)			   # prints 'bacon local'
		spam()                 # prints 'spam local'
		print(eggs)			   # prints 'bacon local'

	eggs = 'global'
	bacon()
	print(eggs) 			   # prints 'global'


def f29():
	# global variables
	# use 'global', if need to specify a variable as global from within a function.
	# in followintg we use a technique to use a global variable by  declaring  and 
	# assining value to that global variable inside of a function, and call the function 
	# when global variable is needed to be used.
	# 
	def spam():
		global eggs
		eggs = 'spam'

	eggs = 'global'
	spam()
	print(eggs)


def f30():
	# Exception Handling
     
	def spam(divideBy):
		try:						# Potential error code is in try clause
			return 42 / divideBy
		except ZeroDivisionError:	# When error is caught in try clause, then it moves to except block, 
		                            # and then gets back to try block and continue the next statement 
		                            # after the statement with error
			print('Error: Invalid argument.')

	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))


def f31():
	# Out Of Function Exception Handling
	# Difference between the folloing code and the previous one:
	# In previous code any errors that occur in function calls in 
	# a try block will also be caught.

	def spam(divideBy):
		return 42 / divideBy

	try:
		print(spam(2))
		print(spam(12))
		print(spam(0))
		print(spam(1))
	except ZeroDivisionError:
		print('Error: Invalid argument.')


def f32():
	# Guessing Game
	import random
	secretNumber = random.randint(1, 20)
	print('I am thinking of a number between 1 and 20.')

	# Ask the player to guess 6 times.
	for guessesTaken in range(1, 7):
		print('Take a guess.')
		guess = int(input())
		
		if guess < secretNumber:
			print('Your guess is too low.')
		elif guess > secretNumber:
			print('Your guess is too high.')
		else:
			break

	# This condition is the correct guess!
	if guess == secretNumber:
		print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
	else:
		print('Nope. The number I was thinking of was ' + str(secretNumber))


def f33():
	# Lists - examples
	print([1, 2, 3])
	print(['cat', 'bat', 'rat', 'elephant'])
	print(['hello', 3.1415, True, None, 42])

	# Getting Individual Values in a List with Indexes
	spam = ['cat', 'bat', 'rat', 'elephant']
	print(spam)
	print(spam[0])
	print(spam[1])
	print(spam[2])
	print(spam[3])
	print(['cat', 'bat', 'rat', 'elephant'][3])
	print('Hello ' + spam[0])
	print('The ' + spam[1] + ' ate the ' + spam[0] + '.')
	print(spam[int(1.0)])

def f34():
	# Lists : list of lists
	spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]	# List of lists
	print(spam)
	print(spam[0][1])
	print(spam[1][4])
	

def f35():
	# Lists : negative indexes
	spam = ['cat', 'bat', 'rat', 'elephant']
	print(spam[-1])     # elephant
	print(spam[-3])     # bat
	print(spam[0:-1])	# ['cat', 'bat', 'rat']
	print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')


def f36():
	# Lists : getting sublists with slices
	spam = ['cat', 'bat', 'rat', 'elephant']
	print(spam[0:4])    # ['cat', 'bat', 'rat', 'elephant']
	print(spam[1:3])	# ['bat', 'rat']
	print(spam[0:-1])	# ['cat', 'bat', 'rat']
	print(spam[:2])		# ['cat', 'bat']
	print(spam[1:])		# ['bat', 'rat', 'elephant']
	print(spam[:])		# ['cat', 'bat', 'rat', 'elephant']

def f37():
	# Lists : getting a list’s length with len()
	spam = ['cat', 'dog', 'moose']
	print(len(spam))  # 3

	
def f38():
	# Lists : changing values in a list with indexes
	spam = ['cat', 'bat', 'rat', 'elephant']
	spam[1] = 'aardvark'
	print(spam)
	spam[2] = spam[1]
	print(spam)
	spam[-1] = 12345
	print(spam)

def f39():
	# Lists: list concatenation and list replication
	x = [1, 2, 3] + ['A', 'B', 'C']
	print(x)
	x = ['X', 'Y', 'Z'] * 3
	print(x)
	spam = [1, 2, 3]
	spam = spam + ['A', 'B', 'C']
	print(spam)


def f40():
	# Help : How to use this program
	os.system('clear')
	text= '''

	Help
	....  

	- At the prompt in main menu, type any number related to 
	  menu item to view that item.
	  Valid numbers are from 1 to the last index number in the 
	  main menu items.


	- each item in main menu list, contains two parts:
	  body of a sample code and the respective output.
	  
	- Some code samples at the output are suppose to interact 
	  with user and prompt for user input.

	- To restart and resetting the script type 'r'

	- To exit the program type exit

	'''
	print(text)
