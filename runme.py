#!/usr/bin/python3
# Author: bm-zi

import os
import codeExamples
import time
import sys
import re

help = '''
    ....
    Help
    ....
    

    ------------- Keys for Main menu prompt ---------------
    The prompts for main menu looks like following:
    Search:
    
    [\]
    When you are in search prompt, you can go to main prompt('>>>'), 
    by typing '\' and once you are in main prompt, press Enter to get 
    back to Search prompt, to navigate through the rolling list of items.

    [space]
    Hit space bar to view the whole item menu at once.

    Any other keys or 'Enter' will roll the menu items in ascending
    order.


    ------------- Keys for main prompt ( >>> ) --------------
    [1..9][0..9]
    Type any number related to menu item to view that item.
    Valid numbers are from 1 to the last index number in the 
    main menu items.

    - each item in main menu list, contains two parts:
      body of a sample code and the respective output.
      
    - Some code samples at the output are suppose to interact 
      with user and prompt for user input.

    [r]  
    To restart and resetting the script type 'r'

    [?] or [help]
    Type in '?' or 'help' to view help !

    [x]
    To exit the program type 'x'.
'''


def restart():
    print('Restarting ... ')
    time.sleep(0.5)
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


def rolling_list():

    def listdisplay(start_line, iterate):
        
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
            print('Welcome to main menu,')
            print('Menu lines No: ', j)
            listdisplay(i, 15)
            print('_' * 68)
            print('For help, first type \'\\\' in below search prompt and then type in \'?\'')
            response = input('Search: ')
            if response == '\\':
                return
            elif not response:
                i = i + 1
                os.system("clear")
            else:
                with open('list') as f:
                    print('')
                    print('Search result: ')
                    for l in f:
                        if re.search(response, l, re.I):
                            print(l.strip())
                        else:
                            continue 

                print('')
                return            
                #input('Press any key to continue! ')

                i = i + 1
                os.system("clear")
        return            
    runner()



while True:
    os.system('clear')
    rolling_list()
    print('')
    i = input(">>> ")

    try:
        if str(i) == 'x':      # type x to exit program
            sys.exit()

        if str(i) == 'r':
            restart()

        if str(i) == '?' or str(i) == 'help':
            os.system('clear')
            print(help)
            input('Press any key to continue -  ')
            continue

        if not i:                  # if no value entered, restart the while loop
            continue

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
        time.sleep(1)

    except AttributeError:        # Caught error when input integer is bigger than list items numbers
        continue
        

