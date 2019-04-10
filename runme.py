#!/usr/bin/python3
# Author: bm-zi

import os
import codeExamples
import time
import sys
import re

def help():
    os.system("clear")
    help = '''Help
    
    |||||||| Keys for Main menu prompt ||||||||||||
    The prompts for main menu looks like following:
    Search in list:
    
    [\]
    When you are in search prompt, you can go to main prompt('# '), 
    by typing '\' or any character and once you are in main prompt, 
    press Enter to get back to Search prompt, to navigate through the 
    rolling list of items.

    [space]
    Hit space bar to view the whole item menu at once.

    [numbers]
    if you type only numbers in search, it opens the list from that item number.
    Any other keys or 'Enter' will roll the browsing list in ascending order.
    
    ||||||||||| Keys for main prompt (# ) ||||||||||||||

    [number]
    Type any number related to browsing list to view the content.
    Valid numbers are from 1 to the last index number in the  main menu items.

    - each item in browsing list, contains two parts:
      Body of a sample code and the respective output.
      
    - Some code samples at the output are suppose to interact 
      with user and prompt for user input.

    [x]
    To exit the program type 'x'.
'''
    print(help)
    input('Press any key to continue!') 
    os.system("clear")

def highlight(text):
    os.system("tput smso")
    print(text)
    os.system("tput rmso")
    

def logo():
    logo = '''┌───────────────────────────────────────────┐
│ Welcome to Interactive Python Programming │
└───────────────────────────────────────────┘''' 
    print(logo)
    #print(time.strftime("%B %d, ") + time.strftime("%H:%M"))



def restart():
    print('Restarting ... ')
    time.sleep(0.50)
    os.execl(sys.executable, sys.executable, * sys.argv)


def displayCode(i):
    flist = open("codeExamples.py").readlines()

    parsing = False
    for line in flist:
        if line.startswith('def f' + str(i + 1) + '()'):
            parsing = False
        if parsing:
            print(line, end='')
        if line.startswith('def f' + str(i) + '()'):
            parsing = True

def listRange(start_line):
    iterate = 15
    start_line = int(start_line) - 1

    test_array = []
    with open('list') as my_file:
        for line in my_file:
            line = line.strip()
            test_array.append(line)

    lines = len(test_array)

    print('_' * 68)

    try:
        lines = len(test_array)
        while iterate > 0 and start_line <= (start_line + 5) and start_line <= lines:
            print(test_array[start_line])
            start_line = start_line + 1
            iterate = iterate - 1
    except IndexError:
        return


def rolling_list():

    def listdisplay(start_line, iterate):
        
        start_line = int(start_line) - 1

        test_array = []
        with open('list') as my_file:
            for line in my_file:
                line = line.strip()
                test_array.append(line)

        lines = len(test_array)

        try:
            lines = len(test_array)
            while iterate > 0 and start_line <= (start_line + 5) and start_line <= lines:
                print(test_array[start_line])
                start_line = start_line + 1
                iterate = iterate - 1
        except IndexError:
            return

    def runner():
        os.system("clear")

        lines = []
        with open('list') as my_file:
            for line in my_file:
                line = line.strip()
                lines.append(line)
     
        i = 1
        j = len(lines)
        
        while i <= j:
            logo()
            print('BROWSING LIST: (' + str(j) + ' items)     ' 
                + time.strftime("%B %d, ") + time.strftime("%H:%M"))
            print()       
            listdisplay(i, 15)
            print()
            highlight('PRESS ENTER TO BROWSE THE LIST, ? FOR HELP')
            response = input('Search in list: ')

            if response == '\\':
                return
            elif response == '?':
                help()
                continue    
            elif response == '':
                i = i + 1
                os.system("clear")
            elif not response:
                i = i + 1
                os.system("clear")
            elif response.isnumeric():
                os.system("clear")
                listRange(response)
                print('_' * 68)
                input('Press any key to continue! ')
                os.system("clear")
            else:
                with open('list') as f:
                    #os.system("clear")
                    print('Search result for \'' + response  + '\' is: ')
                    for l in f:
                        if re.search(response, l, re.I):
                            print(l.strip())
                        else:
                            continue
                print('')
                return
        return
    runner()


#### MAIN PROGRAM BLOCK ####
def mainBlock():
    while True:
        os.system('clear')
        rolling_list()
        print('')
        i = input("# ")

        try:
            if str(i) == 'x':      # type x to exit program
                sys.exit()

            if str(i) == '':
                restart()

            num=int(i)
            varstring1 = 'f' + str(num)
            varstring2 = 'f' + str(num + 1)

            os.system('clear')

            print('|' * 20 + ' CODE EXAMPLE No: ' + str(num) + ' ' + '|' * 20 )
            print()
            displayCode(num)
            print()        
            print('|' * 18 + ' OUTPUT OF CODE No: ' + str(num) + ' ' + '|' * 18 )
            print()
            fct=getattr(codeExamples,varstring1)
            fct()
            print()
            print('==========================')
            print('Press any key to continue!', end='')
            input()
            
        except ValueError:            # Caught error when input is a string
            print('Not an integer!')
            restart()
            time.sleep(1)

        except AttributeError:        # Caught error when input integer is bigger than list items numbers
            os.system("clear")
            print('Number is out of range!')
            time.sleep(1)
            continue

    
mainBlock()   
