#!/usr/bin/python3
# Author: bm-zi

import os
import codeExamples
import time
import sys

'''
use the following command to get a list of indexed functions:

cat searchExamples.py | grep -E 'f[1-9]|f[1-9][0-9]' -A 1 | grep -v def | grep -v ^-- | while read line ; do echo "$i - $line"; let "i=i+1"; done | sed -n 's/\#//p'
'''

def restart():
	print('Restarting ... ')
	time.sleep(1)
	os.execl(sys.executable, sys.executable, * sys.argv)


index='''
1 -  Math Operators
2 -  String concatenation and replication
3 -  First Python Program
4 -  Function len()
5 -  Function str()
6 -  Function str(), int(), float
7 -  input() function
8 -  Boolean data types
9 -  Boolean Operators
10 -  Mixing Boolean and Comparison Operators
11 -  if,elif,else conditional
12 -  while loop
13 -  An Annoying while Loop
14 -  break Statements
15 -  continue statement
16 -  empty value is considered False
17 -  for Loops and the range() Function
18 -  equivalent while loop
19 -  Another for loop example - sum of numbers from 1 to 100
20 -  range() function examples
21 -  import modules
22 -  sys.exit()
23 -  FUNCTIONS
24 -  Function with argument
25 -  return statement
26 -  None
27 -  Optional keywords for functions
28 -  Local and Global Variables with the Same Name
29 -  global variables
30 -  Exception Handling
31 -  Out Of Function Exception Handling
32 -  Guessing Game
33 -  Lists : examples
34 -  Lists : list of lists
35 -  Lists : negative indexes
36 -  Lists : getting sublists with slices
37 -  Lists : getting a list’s length with len()
38 -  Lists : changing values in a list with indexes
39 -  Lists: list concatenation and list replication
40 -  Help : How to use this program
'''

while True:
	os.system('clear')
	print(index)  		# Display a list of codes sample names 

	print('================================')
	i = input("Enter a number to view the item: ")

	try:
		if str(i) == 'exit':      # type exit to exit program
			sys.exit()

		if str(i) == 'r':
			restart()

		if not i:				   # if no value entered, restart the while loop
			continue

		num=int(i)
		varstring1 = 'f' + str(num)
		varstring2 = 'f' + str(num + 1)

		os.system('clear')
		print('-------------------- CODE EXAMPLE No ' + str(num) + ' --------------------')
		command = 'cat codeExamples.py | sed -n \'/def\ ' + varstring1 + '()/,/def\ ' + varstring2 + '/p\' | grep -v '  + varstring1 + '| grep -v ' + varstring2
		os.system(command)
		print('-------------------- CODE No ' + str(num) + ' OUTPUT --------------------')
		fct=getattr(codeExamples,varstring1)
		fct()
		print()
		print('==========================')
		print('Press any key to continue!', end='')
		input()
		
	except ValueError:  		  # Caught error when input is a string
		print('Not an integer!')
		time.sleep(1)

	except AttributeError:		  # Caught error when input integer is bigger than list items numbers
		continue
		
