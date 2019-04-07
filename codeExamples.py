#!/usr/bin/env  python
# -*- coding: utf-8 -*-

# Author: bm-zi


import os

def f1():
    # Math Operators
    # --- CHAPTER 1 --- 
    print(2+2)  # 4
    print(2)    # 2     
    print(2 + 3 * 6)    # 20
    print((2 + 3) * 6)  # 30
    print(48565878 * 578453)    # 28093077826734
    print(2 ** 8)   # 256
    print(23 / 7)   # 3.2857142857142856
    print(23 // 7)  # 3
    print(23 % 7)   # 2
    print(2    +    2)  # 4
    print((5 - 1) * ((7 + 1) / (3 - 1)))  # 16.0
    print()  # blank line in python3


def f2():
    # String concatenation and replication
    print('Alice' + 'Bob') # AliceBob
    print('Alice' * 5)  # AliceAliceAliceAliceAlice


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
    print(42 == 42.0)    # True
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
    print(2 != 3)     # True
    print(2 != 2)     # False 
    
    # The == and != operators can actually work with values of any data type.
    
    print('hello' == 'hello')   # True
    print('hello' == 'Hello')   # False
    print('dog' != 'cat')       # True
    print(True == True)         # True
    print(True != False)        # True
    print(42 == 42.0)           # True
    print(42 == '42')           # False
    
    print(42 < 100)         # True
    print(42 > 100)         # False
    print(42 < 42)          # False
    
    eggCount = 42
    print(eggCount <= 42)   # True
    
    myAge = 29
    print(myAge >= 10)      # True

def f9():
    # Boolean Operators
    # and operator
    print(True and True)    # True
    print(True and False)   # False
    print(False and True)   # False
    print(False and False)  # False
    
    
    # or operator
    print(True or True)     # True
    print(True or False)    # True
    print(False or True)    # True
    print(False or False)   # False
    
    # not operator
    print(not True)     # False
    print(not False)    # True

def f10():
    # Mixing Boolean and Comparison Operators
    print((4 < 5) and (5 < 6))      # True
    print((4 < 5) and (9 < 6))      # False
    print((1 == 2) or (2 == 2))     # True
    print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)     # True


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
    # break Statements, breaks the loop
    while True:
        print('Please type your name.')
        name = input()
        if name == 'your name':
            break
    print('Thank you!')


def f15():
    # continue statement, keeps running the loop start from begining
    while True:
        print('Who are you?')
        name = input()
        if name != 'Joe':
            continue   # restart the loop      
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()
        if password == 'swordfish':
            break      # stops the loop
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
    # functions like print(), input() , and len() are builtin fuctions; 
    # No need to import them.
    # function like randint() are from standard library modules that 
    # has to be imported

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
    print('World')                         # By defualt print prints a newline after printing 
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
        print(eggs)            # prints 'bacon local'
        spam()                 # prints 'spam local'
        print(eggs)            # prints 'bacon local'

    eggs = 'global'
    bacon()
    print(eggs)                # prints 'global'


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
        try:                        # Potential error code is in try clause
            return 42 / divideBy
        except ZeroDivisionError:   # When error is caught in try clause, then it moves to except block, 
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
    spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]   # List of lists
    print(spam)
    print(spam[0][1])
    print(spam[1][4])
    

def f35():
    # Lists : negative indexes
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[-1])     # elephant
    print(spam[-3])     # bat
    print(spam[0:-1])   # ['cat', 'bat', 'rat']
    print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')


def f36():
    # Lists : getting sublists with slices
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[0:4])    # ['cat', 'bat', 'rat', 'elephant']
    print(spam[1:3])    # ['bat', 'rat']
    print(spam[0:-1])   # ['cat', 'bat', 'rat']
    print(spam[:2])     # ['cat', 'bat']
    print(spam[1:])     # ['bat', 'rat', 'elephant']
    print(spam[:])      # ['cat', 'bat', 'rat', 'elephant']

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

    # It is like strings concatenation and replication
    x = [1, 2, 3] + ['A', 'B', 'C']
    print(x)
    x = ['X', 'Y', 'Z'] * 3
    print(x)
    spam = [1, 2, 3]
    spam = spam + ['A', 'B', 'C']
    print(spam)


def f40():
    # Lists : removing values from lists with del statements
    spam = ['cat', 'bat', 'rat', 'elephant']
    del spam[2]
    print(spam)
    del spam[2]
    print(spam)
    

def f41():
    # Lists : working with lists

    # instead of using many varibales use lists for data entry
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name] # list concatenation
    print('The cat names are:')
    for name in catNames:
        print('    ' + name)


def f42():
    # Lists : using for loops

    print('simple for loop : ')
    for i in range(4):
        print(i)

    print('using for loop with list : ')
    for i in [0, 1, 2, 3]:
        print(i)

    print('technique of using range(len(someList)) with a for loop : ')
    supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


def f43():
    # Lists : in and not in operators

    # determine whether a value is or isn’t in a list
    print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
    spam = ['hello', 'hi', 'howdy', 'heyas']
    print(spam)
    print('cat' in spam)
    print('howdy' not in spam)
    print('cat' not in spam)

    print ('...')
    print('Sample program to check if value is in list : ')
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    print(myPets)
    print('Enter a pet name:')
    name = input()
    if name not in myPets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.') 


def f44():
    # Lists : multiple assignment trick
    cat = ['fat', 'black', 'loud']
    size = cat[0]
    color = cat[1]
    disposition = cat[2]
    print(cat)

    print('...  ...  ...  ... ')
    cat = ['fat', 'black', 'loud']
    size, color, disposition = cat
    print(cat)


def f45():
    # Augmented assignment operators

    '''
    statement          Equivalent
    spam = spam + 1    spam += 1
    spam = spam - 1    spam -= 1
    spam = spam * 1    spam *= 1
    spam = spam / 1    spam /= 1
    spam = spam % 1    spam %= 1
    ''' 

    spam = 42
    spam = spam + 1
    print(spam)

    spam = 42
    spam += 1
    print(spam)

    spam = 'Hello'
    spam += ' world!'
    print(spam)

    bacon = ['Zophie']
    bacon *= 3
    print(bacon)

def f46():
    # Lists : finding a Value in a list with the index() method

    # Methods are the same as functoions, except that is called on value
    # Each data type has its own set of methods.
    # list data type, for ­example, has several useful methods for finding, 
    # adding, removing, and manipulating values in a list.

    spam = ['hello', 'hi', 'howdy', 'heyas']
    print(spam.index('hello'))
    print(spam.index('heyas'))

    # When there are duplicates of the value in the list, 
    # the index of its first appearance is returned.

    spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
    print(spam.index('Pooka'))


def f47():
    # Methods - adding values to lists with append() and insert() methods
    
    spam = ['cat', 'dog', 'bat']
    spam.append('moose')
    print(spam)

    spam = ['cat', 'dog', 'bat']
    spam.insert(1, 'chicken')
    print(spam)



def f48():
    # Lists : removing values from lists with remove()
    spam = ['cat', 'bat', 'rat', 'elephant']
    spam.remove('bat')
    print(spam)

    # If the value appears multiple times in the list, 
    # only the first instance of the value will be removed

    spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
    spam.remove('cat')
    print(spam)


def f49():
    # List : sorting the values in a list with the sort() method
    spam = [2, 5, 3.14, 1, -7]
    spam.sort()
    print(spam)

    spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    spam.sort()
    print(spam)

    # You can also pass True for the reverse keyword argument to have sort()
    # sort the values in reverse order
    spam.sort(reverse=True)
    print(spam)

    # note (1) :
    # You cannot write: spam = spam.sort() ,
    # sort() method sorts the list in place
    # note (2) :
    # cannot sort lists that have both number and string
    # note (3) :
    # sort() uses “ASCIIbetical order” rather than actual alphabetical

    spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
    spam.sort()
    print(spam)

    # To sort in alphabetic order:
    spam = ['a', 'z', 'A', 'Z']
    spam.sort(key=str.lower)
    print(spam)


def f50():
    # magic 8 ball with a list

    # much more elegant version of previous 8 ball
    import random
    messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
    print(messages[random.randint(0, len(messages) - 1)])


def f51():
    # list-like types: strings and tuples

    '''
    You can consider a string to be a "list" of single text characters.
    Then you can use indexing; slicing; and using them with for loops, 
    with len() , and with the in and not in operators.
    '''
    name = 'Zophie'
    print(name[0])

    print(name[-2])
    print(name[0:4])
    print('Zo' in name)
    print('z' in name)
    print('p' not in name)

    for i in name:
        print('* * * ' + i + ' * * *')

def f52():
    # mutable and immutable data types

    # Lists can have values added, removed, or changed. (mutable)
    # Strings are not. (immutable)

    name = 'Zophie a cat'
    # name[7] = 'the'   # this generates error
    newName = name[0:7] + 'the' + name[8:12]
    print(name)
    print(newName)

    eggs = [1, 2, 3]
    eggs = [4, 5, 6] # The list value in eggs isn’t being changed here; is overwriiten.
    print(eggs)
    
    print('The actula modification is as following: ')
    eggs = [1, 2, 3]
    del eggs[2]
    del eggs[1]
    del eggs[0]
    eggs.append(4)
    eggs.append(5)
    eggs.append(6)
    print(eggs)

def f53():
    # tuple data type

    # tuples are like lists but use () instead aof []
    # tuples are like strings, cannot have their values modified, appended, or removed.

    eggs = ('hello', 42, 0.5)
    # eggs[1] = 99   # this generates error

    # If you have only one value in your tuple, you can indicate this 
    # by placing a trailing comma
    print(type(('hello',)))
    print(type(('hello')))

    '''tuples advantages:
    . When you don't want the values to be changed.(unlike the list) 
    . They are faster than lists
    ''' 
    print('Converting Types with the list() and tuple() Functions')
    print(tuple(['cat', 'dog', 5]))
    print(list(('cat', 'dog', 5)))
    print(list('hello'))

def f54():
    # references

    # assignment for strings and integers value
    spam = 42
    cheese = spam
    spam = 100
    print('spam has different value than cheese: ')
    print(spam)
    print(cheese) # cheese didn't chage

    # assignment foe lists is different, actually we are assiging a 
    # list reference to the variable

    spam = [0, 1, 2, 3, 4, 5]
    cheese = spam
    cheese[1] = 'Hello!'
    print('spam and cheese have the same value: ')
    print(spam)
    print(cheese)

    '''
    When you create the list, you assign a reference to it in the spam 
    variable. But the next line copies only the list reference in spam 
    to cheese , not the list value itself.
    list variables don’t actually contain lists—they contain references
    to lists.
    '''


def f55():
    # Passing References

    '''
    When a function is called, the values of the arguments are copied 
    to the parameter variables. For lists and dictionaries, this means 
    a copy of the reference is used for the parameter.
    '''

    def eggs(someParameter):
        someParameter.append('Hello')
    
    spam = [1, 2, 3]
    eggs(spam)
    print(spam)

    '''
    Notice that when eggs() is called, a return value is not used to 
    assign a new value to spam. Instead, it modifies the list in place, directly.

    Even though spam and someParameter contain separate references, they
    both refer to the same list. This is why the append('Hello') method call
    inside the function affects the list even after the function call has returned.
    '''

def f56():
    # The copy Module’s copy() and deepcopy() Functions

    '''
    copy.copy() , makes a duplicate copy of a mutable value like a list or dictionary, 
    not just a copy of a reference.
    '''

    import copy
    spam = ['A', 'B', 'C', 'D']
    cheese = copy.copy(spam)  # creates a second list that can be modified 
                              # ­independently of the first.
    cheese[1] = 42
    print('copy.copy')
    print(spam)
    print(cheese)

    milk = copy.deepcopy(cheese)
    milk[1] = 52
    print('copy.deepcopy')
    print(spam)
    print(cheese)
    print(milk)
 
def f57():
    grid = [['.','.','.','.','.','.'],
            ['.','0','0','.','.','.'],
            ['0','0','0','0','.','.'],
            ['0','0','0','0','0','.'],
            ['.','0','0','0','0','0'],
            ['0','0','0','0','0','.'],
            ['0','0','0','0','.','.'],
            ['.','0','0','.','.','.'],
            ['.','.','.','.','.','.']]

    print(grid)
            
def f58():
    # Dictionary Data Type
    myCat = {'size': 'fat', 'color': 'grey', 'disposition': "loud" }
    print(myCat['size'])
    print('My cat has ' + myCat['color'] + ' fur.')
    
    # Dictionaries can use integer values as keys, like lists.
    # There is no item order in dictionaries.
    spam = {12345: 'Luggage Combination', 42: 'The Answer'}
    print(spam)

    print('Dictionaries vs. Lists')
    spam = ['cats', 'dogs', 'moose']
    bacon = ['dogs', 'moose', 'cats']
    print(spam == bacon)

    eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
    print(eggs == ham)


def f59():
    # program to store data
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')
            print(birthdays)

def f60():
    print(' ')

def f61():
    print(' ')

def f62():
    print(' ')

def f63():
    print(' ')

def f64():
    print(' ')

def f65():
    print(' ')

def f66():
    print(' ')

def f67():
    print(' ')

def f68():
    print(' ')

def f69():
    print(' ')

def f70():
    print(' ')

