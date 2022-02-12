import random
from potato import*
from wheat import*
from sheep import*
from cow import*
from crop_sim import*
from animal import*



class field:
    def __init__(self,max_animals,max_crops):
        self._crops=[]
        self._animals=[]
        self._max_animals=max_animals
        self._max_crops=max_crops

    def plant_crop(self,crop):
        if len(self._crops)<self._max_crops:
            self._crops.append(crop)
            return True
        else:return False

    def add_animal(self,animal):
        if len(self._animals)<self._max_animals:
            self._animals.append(animal)
            return True
        else: return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report=[]
        animal_report=[]
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {'crop':crop_report,'animals':animal_report}

    def report_needs(self):
        food=0
        light=0
        water=0
        for crop in self._crops:
            needs=crop.needs()
            if needs['light need']>light:light=needs['light need']
            if needs['water need']>water:water=needs['water need']
        for animal in self._animals:
            needs=animal.needs()
            food+=needs['food need']
            if needs['water need']>water:water=needs['water need']
        return {'food':food,'light':light,'water':water}


    def grow(self,light,food,water):
        if len(self._crops)>0:
            for crop in self._crops:
                crop.grow(light,water)
                
        if len(self._animals)>0:
            food_required=0
            for animal in self._animals:
                needs=animal.needs()
                food_required+=needs['food need']

            if food>food_required:
                additional_food=food-food_required
                food =food_required
            else:additional_food=0
            
            for animal in self._animals:
                needs=animal.needs()
                if food>=needs['food need']:
                    food-=needs['food need']
                    feed = needs['food need']
                    if additional_food>0:
                        additional_food-=1
                        feed+=1
                    animal.grow(feed,water)
        
def auto_grow(self,days):
    for day in range(days):
        light=random.randint(1,10)
        water=random.randint(1,10)
        food=random.randint(1,10)
        field.grow(self,light,food,water)

def manual_grow(field):
    valid=False
    while not valid:
        try:
            light=int(input('Light value?'))
            if 1<=light<=10:valid=True
            else:print('not valid')
        except ValueError:
            print('not valid')
    valid=False
    while not valid:
        try:
            water=int(input('Water value?'))
            if 1<=water<=10:
                valid=True
            else:print('not valid')
        except ValueError:
            print('not valid')
    valid=False
    while not valid:
        try:
            food=int(input('food value?'))
            if 1<=food<=100:
                valid=True
            else:print('not valid')
        except ValueError:
            print('not valid')    
    field.grow(light,food,water)

    
        
def display_crops(crop_list):
    print('crops in this field:')
    pos=1
    for crop in  crop_list:
        print('{0:>2}.{1}'.format(pos,crop.report()))
        pos+=1

def display_animals(animal_list):
    print('Animals in field')
    pos=1
    for animal in animal_list:
        print('{0:>2}.{1}'.format(pos,animal.report()))
        pos+=1
    
def select_crop(length_list):
    valid=False
    while not valid:
        selected =int(input('please select a crop'))
        if selected in range(1,length_list+1):valid=True
        else: print('please select a valid option')
    return selected-1

def select_animal(length_list):
    valid=False
    while not valid:
        selected =int(input('please select an animal'))
        if selected in range(1,length_list+1):valid=True
        else: print('please select a valid option')
    return selected-1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop=select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal=select_animal(len(field._animals))
    return field.remove_animal(selected_animal)

            
def display_crop_menu():
    print('which crop would you like to add')
    print('1. potato\n2. wheat')
    print('0. I dont want to add a crop (return to main menu)')

def display_animal_menu():
    print('which crop would you like to add')
    print('1. cow\n2. sheep')
    print('0. I dont want to add a crop (return to main menu)')

def display_main_menu():
    print('1. plant new crop\n2. harvest a new crop\n3. add animal \n4. remove animal\n5. grow field manually over 1 day\n6. grow field automatically over 30 days\n7. report feild status\n8. exit program')

def get_menu_choice(lower,upper):
    valid=False
    while not valid:
        try:
            choice=int(input('option?'))
            if lower<=choice<=upper:
                valid=True
            else:print('not valid')
        except ValueError:
            print('not valid')
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice=get_menu_choice(0,2)
    if choice==1:
        if field.plant_crop(potato()):
            print('crop planted')
        else:print('feild is full')
    elif choice==2:
        if field.plant_crop(wheat()):print('crop planted')
        else:print('feild is full')
        

def add_animal_to_field(field):
    display_animal_menu()
    choice=get_menu_choice(0,2)
    name=input('name of your animal?')
    if choice==1:
        if field.add_animal(cow(name)):
            print('animal added')
        else:print('feild is full')
    elif choice==2:
        if field.add_animal(sheep(name)):print('animal added')
        else:print('feild is full')

def manage_field(field):
    print('this is the field management program')
    exit = False
    while not exit:
        display_main_menu()
        option=get_menu_choice(0,8)
        if option==1:plant_crop_in_field(field)
        elif option==2:
            removed_crop = harvest_crop_from_field(field)
            print('you removed crop:{0}'.format(removed_crop))
        elif option==3: add_animal_to_field(field)
        elif option==4:
            removed_animal=remove_animal_from_field(field)
            print('you removed animal:{0}'.format(removed_animal))
        elif option==5:manual_grow(field)
        elif option==6:auto_grow(field,30)
        elif option==7:print(field.report_contents())
        elif option==8:exit=True
    print('=======END OF PROGRAM======')
            
        
        


def main():
    new_field= field(5,2)
    manage_field(new_field)

if __name__=='__main__':
    main()
