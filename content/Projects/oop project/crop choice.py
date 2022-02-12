from wheat import *
from potato import *
from cow import*
from sheep import*

def display_menu():
    pass

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
    print('which crop would you like to create\n1. Potato\n2. Wheat')
    choice = select_option()
    if choice==1:new_crop=potato()
    elif choice==2: new_crop=wheat()
    return new_crop

def create_animal(animal_name):
    print('which animal would you like to chose\n1. Cow\n2. Sheep')
    choice =select_option()
    if choice == 1:
        new_animal=cow(animal_name)
    elif choice==2:
        new_animal=sheep(animal_name)
    return new_animal

animal_exists=False
def main():
    global animal_exists
    
    new_crop = create_crop()
    manage_crop(new_crop)
    
    choice = input('Would you like to add an animal? (y/n)')
    if choice == 'y':
        animal_name=str(input('The animals name'))
        new_animal=create_animal(animal_name)
        animal_exists==True
        manage_animal(new_animal)
        
    if animal_exists==True:
        manage_animal(new_animal)

if __name__ == '__main__':
    main()
