#!/usr/bin/python3
# Author: bm-zi

import os
import functions
import time
import sys
import re
import pprint

def help():
    resetScreen()
    help = '''
    |||||||||||||||||||||||| Help Manual |||||||||||||||||||||||||

    ..............................................................
    ||||||||||||| Keys defined for Search prompt |||||||||||||||||
    ..............................................................

    The prompts for main menu looks like as following:
    Search in list:
    
    [\\ | + | - | / | * | . | Space ] 
    When you are in search prompt, you can go to main prompt('# '), 
    by typing any of above characters and once you are in main pr-
    ompt, press 'Enter' to get back to Search prompt, to navigate 
    through the rolling list of items.

    [Numbers]
    if you type only numbers in search, it opens the list from th-
    at item number. Any other keys or 'Enter' will roll the brows-
    ing list in ascending order.
    
    ..............................................................
    |||||||||||||||| Keys for main prompt (# ) |||||||||||||||||||
    ..............................................................
    
    [Numbers]
    Type any number related to browsing list to view the content.
    Valid numbers are from 1 to the last index number in the  main
    menu items.

    - Each item in browsing list, contains two parts, body of the 
      code and the respective output.
    - Some code samples at the output are suppose to interact 
      with user and prompt for user input.
    
    [q | Q | x | X | quit | exit]
    To exit the program either type 'x' in main prompt, or type in
    '\\\\' in seach prompt.'''

    tempFile = open('temp', 'w')
    tempFile.write(help)
    tempFile.close()

    os.system('less temp')
    os.unlink('temp')
    resetScreen()


def resetScreen():
    # Resize and clear the screen
    print('\x1b[8;30;90t')
    os.system('clear')


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


def searchFiles(response):
    resetScreen()          
    print('SEARCH ALL FUNCTIONS FOR PATTERN : \'' + response  + '\' ')
    print('==================================')
    with open('functions.py') as f2:
        defLines = []
        matches = []
        matchline = []
        for lineno, line in enumerate(f2, 1):
            if line.startswith('def'):
                defLines.append(lineno) # + ' - ' + line)
            if re.search(response, line, re.I):
                matches.append(lineno)
                matchline.append(str(lineno) + ' - ' + str(line))
    f2.close()
    
    resultList = []
    for i in range(len(matches)):
        for j in range(len(defLines)):
            if matches[i] > defLines[j] and matches[i] < defLines[j+1]:
                resultList.append(defLines[j])

    newlist = []
    for i in resultList:
      if i not in newlist:
        newlist.append(i)
        
    items = []
    fp = open("functions.py")
    for i, line in enumerate(fp):
        for j in range(len(newlist)):
            if newlist[j] == i+1:
                items.append(line)  
            
    fp.close()
    
    itemlist = []
    for i in range(len(items)):
        pat = re.compile(r'\d+')
        mat = pat.search(items[i])
        itemlist.append(mat.group())

        
    for i in range(len(itemlist)):
        with open('list') as f:
            for l in f:
                if l.startswith(itemlist[i]):
                    print(l.strip())
        f.close()

    # print('\nSearch pattern in source file:')
    # print('................................')    
    # for i in range(len(matchline)):
    #     print(matchline[i], end='')
            

    with open('list') as f1:
        print('\nMAIN MENU SERACH RESULT FOR PATTERN: \'' + response  + '\' ')
        print('====================================')
        for l in f1:
            if re.search(response, l, re.I):
                print(l.strip())
    f1.close()


def lineCount(fileName):
    with open(fileName) as f:
                line_count = 0
                for line in f:
                    line_count += 1

    return line_count

def restart():
    print('Restarting Program ... ')
    time.sleep(1)
    os.execl(sys.executable, sys.executable, * sys.argv)


def displayCode(i):
    flist = open("functions.py").readlines()

    lines = []
    parsing = False
    for line in flist:
        if line.startswith('def f' + str(i + 1) + '()'):
            parsing = False
        if parsing:
            # print(line, end='')
            lines.append(line)
        if line.startswith('def f' + str(i) + '()'):
            parsing = True

    return lines
            

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

    def runner(stln):
        resetScreen()

        lines = []
        with open('list') as my_file:
            for line in my_file:
                line = line.strip()
                lines.append(line)
     
        i = int(stln)
        j = len(lines)
        
        while i <= j:
            logo()
            print('BROWSING LIST: (' + str(j) + ' items)     ' 
                + time.strftime("%B %d, ") + time.strftime("%H:%M"))
            print()
            listdisplay(i, 10)
            print()
            highlight('PRESS ENTER TO BROWSE THE LIST, ? FOR HELP')
            response = input('Search in menu for: ')
            print()

            if response == '\\' or \
                response == '*' or \
                response == '+' or \
                response == '-' or \
                response == '/' or \
                response == '.' or \
                response == ' ': 
                return
            elif response == '\\\\':
                sys.exit()
            elif response == '?':
                help()
                continue
            elif response == '':
                i = i + 1
                resetScreen()
            elif not response:
                i = i + 1
                resetScreen()
            elif response.isnumeric():
                resetScreen()
                runner(response)
                break
            else:
                '''
                with open('list') as f:
                    resetScreen()
                    print('Result for searching \'' + response  + '\' : ')
                    for l in f:
                        if re.search(response, l, re.I):
                            print(l.strip())
                        else:
                            continue
                print('')
                return
                '''
                searchFiles(response)
                print('')
                return

        return
    runner(1)

############################
#### MAIN PROGRAM BLOCK ####
############################
def mainBlock():
    while True:
        resetScreen()
        rolling_list()
        print('')
        i = input("# ")

        try:
            # exit program
            if str(i) == 'x' or \
                str(i) == 'X' or \
                str(i) == 'q' or \
                str(i) == 'Q' or \
                str(i) == 'quit' or \
                str(i) == 'exit':      
                sys.exit()

            if str(i) == '':
                restart()

            num=int(i)
            varstring1 = 'f' + str(num)
            varstring2 = 'f' + str(num + 1)

            resetScreen()

            print('|' * 20 + ' CODE EXAMPLE No: ' + str(num) + ' ' + '|' * 20 )
            
            head1 = '|' * 20 + ' CODE EXAMPLE No: ' + str(num) + ' ' + '|' * 20 + '\n'
            tempFile = open('temp', 'a')
            tempFile.write(head1)
            lines = displayCode(num)
            for ln in lines:
                tempFile.write(ln)
            tempFile.close()
    
            lc = lineCount('temp')
             
            if lc > 10:
                resetScreen()
                os.system('less temp')
                tempFile = open('temp')
                content = tempFile.read()
                tempFile.close()
                print(content)
            else:
                resetScreen()
                tempFile = open('temp')
                content = tempFile.read()
                tempFile.close()
                print(content)

            os.unlink('temp')
            print('|' * 18 + ' OUTPUT FOR CODE NO: ' + \
                str(num) + ' ' + '|' * 18 )
            fct=getattr(functions, varstring1)
            fct()
            print('|' * 61)
            print('Press any key to continue!', end='')
            input()
        
        # Caught error when input is a string:    
        except ValueError:
            print('Not an integer!')
            restart()
            time.sleep(1)

        # Caught error when input integer is bigger than list 
        # items numbers:    
        except AttributeError:
            print('Either entered number is out of range,\nor function ' 
                + varstring1 + ' might have some errors!\n')
            
            input('Press any key to continue!')
            continue

mainBlock()