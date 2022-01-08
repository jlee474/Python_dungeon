# library for system commands

# system object for exit command
import sys
# to allow clear screen
from os import system, name

def clear():
    
    # for windows 
    if name == 'nt':
        _ = system('cls') # the _ prevents 0 from displaying
    # for mac and linux (here, os.name is 'posix')
    else:
        _ = system('clear')

def exit():
    sys.exit()