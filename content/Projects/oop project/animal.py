import random

class animal():
    def __init__(self,growth_rate,water_need,food_need,name):
        self._weight=10
        self._days_growing=0
        self._growth_rate=growth_rate
        self._water_need=water_need
        self._food_need=food_need
        self._status='baby'
        self._type='generic'
        self._name=name
    def needs(self):
        return {'food need':self._food_need,'water need':self._water_need}

    def report(self):
        return {'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing,'Name:':self._name}

    def update_status(self):
        if self._weight>100:self._status='old'
        elif self._weight>80:self._status='mature'
        elif self._weight>40:self._status='young'
        elif self._weight>20:self._status='very young'
        elif self._weight==0:self._status='baby'

    def grow(self,food,water):
        if food>= self._food_need and water >= self._water_need:self._growth +=self._growth_rate

        self._days_growing+=1
        self.update_status()

def auto_grow(animal,days):
    for day in range(days):
        food=random.randint(1,10)
        water=random.randint(1,10)
        crop.grow(light,water)

def manual_grow(animal):
    valid=False
    while not valid:
        try:
            food=int(input('food value?'))
            if 1<=food<=10:valid=True
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
    animal.grow(food,water)

def get_menu_choice():
    option_valid=False
    while not option_valid:
            try:
                choice=int(input('option (1,2,3,0)'))
                if 0<=option_valid<=3:option_valid=True
                else:print('not valid')
            except ValueError:
                print('not valid')
    return choice
def display_menu():
    print('1. manually grow\n2. grow automatically\n3. report status\n0.exit')
    

def manage_animal(animal):
    noexit=True
    while noexit:
        display_menu()
        option=get_menu_choice()
        if option==1:manual_grow(animal)
        elif option==2:auto_grow(animal,30)
        elif option==3:print(animal.report())
        elif option==0:noexit=False



def main():
    new_animal=animal(3,5,5,'cow1')
    print(animal.needs(new_animal))
    print(animal.report(new_animal))

if __name__=='__main__':
    main()
