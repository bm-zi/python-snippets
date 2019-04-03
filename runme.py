#!/usr/bin/python3
# Author: bm-zi

import os
import codeExamples
import time
import sys


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

        print('_' * 60)

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
            print('Main menu')    
            print('items No: ', j)
            listdisplay(i, 20)
            print('_' * 60)
            response = input('Go to prompt [p]: ')
            if response == 'p':
                return
            else:    
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
        if str(i) == 'exit':      # type exit to exit program
            sys.exit()

        if str(i) == 'r':
            restart()

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
        

