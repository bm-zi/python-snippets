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

    f[numbers]
    If try this format(for example f45, f67 or 204), then the con-
    tent of the respective functions will be displayed, fetching -
    the content of the function from the file functions.py
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

# ...................
# Function exitProg()
# ...................
def exitProg():
    # This function Removes all files and folders in current work-
    # ing direcctory, except of files runme.py, functions.py and -
    # file list

    import os, shutil

    folder = '.'  # Current working directory

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path) and \
                not file_path == './runme.py' and  \
                not file_path == './list' and  \
                not file_path == './functions.py':
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    os.system('clear')
    sys.exit()

# ......................
# Function resetScreen()
# ......................
def resetScreen():
    # This function resizes the terminal and clears the screen
    print('\x1b[8;30;90t')
    os.system('clear')

# ....................
# Function highlight()
# ....................
def highlight(text):
    # This function highlights the string argument 'text' and will
    # print out the string in bold
    os.system("tput smso")
    print(text)
    os.system("tput rmso")

# ...............    
# Function logo()
# ...............
def logo():
    # This function prints the program title and introduction

    logo = '''┌───────────────────────────────────────────┐
│ Welcome to Interactive Python Programming │
└───────────────────────────────────────────┘''' 
    print(logo)
    #print(time.strftime("%B %d, ") + time.strftime("%H:%M"))

# ..........................
# Function displayFunction()
# ..........................
def displayFunction(fnum):
    # This function gets the content of the function f[fnum] from 
    # within file functions.py and prints that content

    # In following loop, extract the content between definition of
    # function f(n) and the next following function f(n+1)x
    with open('functions.py') as infile, open('temp', 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip().startswith('def f'+ str(fnum) +'():'):
                copy = True
            elif line.strip().startswith('def f'+ str(int(fnum)+1) +'():'):
                copy = False
            elif copy:
                outfile.write(line)
    infile.close()
    outfile.close()

    # prepend a line to temporary output file temp
    firstline = '    Content for function f' + str(fnum) + '\n' + \
                '    ==========================' + '\n\n'

    open('tempfile', 'w').write( firstline + open('temp', 'r').read())
    os.rename('tempfile', 'temp')
    resetScreen()
               
    os.system('less temp')    
    os.unlink('temp')

# ......................
# Function searchFiles()
# ......................
def searchFiles(response):
    # This function does two searches in files functions.py and -
    # file list looking for the pattern as argument passwd to this
    # functioin, 'response'

    #
    # Search in file functions.py
    #
    resetScreen() 
    print('SEARCH ALL FUNCTIONS FOR PATTERN : \'' +response+'\' ')
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
    
    #        
    # Search in file list
    # 
    with open('list') as f1:
        print('\nMAIN MENU SERACH RESULT FOR PATTERN: \'' + \
            response  + '\' ')
        print('====================================')
        for l in f1:
            if re.search(response, l, re.I):
                print(l.strip())
    f1.close()

# ....................
# Function lineCount()
# ....................
def lineCount(fileName):
    # This function returns the number of the lines for the file,
    # passed as the argument to this function

    with open(fileName) as f:
                line_count = 0
                for line in f:
                    line_count += 1

    return line_count

# ..................
# Function restart()
# ..................
def restart():
    # This function restarts the program, to initial state

    print('Restarting Program ... ')
    time.sleep(1)
    os.execl(sys.executable, sys.executable, * sys.argv)

# ......................
# Function displayCode()
# ......................
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

# .....................    
# Function rolling_list
# .....................
def rolling_list():
    # This function has two nested functions: listDisplay() and -
    # runner(), that handles all operation based on user input in
    # search prompt, having the form of 'Search in menu for: '

    def listdisplay(start_line, iterate):
        # This function returns a list of items reading from file 
        # list. The passed arguments, specify how many items will 
        # be displayed, from starting item number(start_line)
        
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
        # This function actions based on the user input and will -
        # iterate the list of items ...
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
            elif re.match(r'^f[1-7]', response):
                reObj = re.compile(r'(f)(\d+)')
                mo = reObj.search(response)
                item = mo.group(2)
                displayFunction(item)
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
                searchFiles(response)
                print('')
                return

        return
    runner(1)

# ....................
# Function mainBlock()
# ....................
def mainBlock():
    # This function is building up the main loop of the program and
    # handles all operations, based on user input received in main
    # prompt with the form of '# '
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
                exitProg()

            if str(i) == '':
                restart()

            num=int(i)
            varstring1 = 'f' + str(num)
            varstring2 = 'f' + str(num + 1)

            resetScreen()

            print('|' * 20 + ' CODE EXAMPLE No: ' + str(num) + \
                 ' ' + '|' * 20 )
            
            head1 = '|' * 20 + ' CODE EXAMPLE No: ' + str(num) + \
                    ' ' + '|' * 20 + '\n'

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
        
        # Catching error when input is a string:
        except ValueError:
            print('Not an integer!')
            restart()
            time.sleep(1)

        # Catching error when input integer is bigger than list 
        # items numbers:
        except AttributeError:
            print('Either entered number is out of range,\nor function ' 
                + varstring1 + ' might have some errors!\n')
            
            input('Press any key to continue!')
            continue

mainBlock()