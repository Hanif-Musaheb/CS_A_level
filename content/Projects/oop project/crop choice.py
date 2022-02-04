from wheat import *
from potatoe import *

def display_menu():
    print('which crop would you like to create\n1. Potato\n2.wheat')

def select_option():
    valid_option=False
    while not valid_option:
        try:
            choice=int(input('option selected'))
            if choice in (1,2):
                valid_option=True
            else:print('enter valid option')
        except ValueError:
            print('enter valid option')
    return choice

def create_crop():
    display_menu()
    if choice==1:
        new
    
