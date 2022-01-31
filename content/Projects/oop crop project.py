import random

class crop():
    def __init__(self,growth_rate,light_need,water_need):
        self._growth=0
        self._days_growing=0
        self._growth_rate=growth_rate
        self._light_need=light_need
        self._water_need=water_need
        self._status='seed'
        self._type='generic'

    def needs(self):
        return {'light need':self._light_need,'water need':self._water_need}
    
    def report(self):
        return {'type':self._type,'status':self._status,'growth':self._growth,'days gorwing':self._days_growing}

    def update_status(self):
        if self._growth>15:self._status='old'
        elif self._growth>10:self._status='mature'
        elif self._growth>5:self._status='young'
        elif self._growth>0:self._status='seedling'
        elif self._growth==0:self._status='seed'

    def grow(self,light,water):
        if light>= self._light_need and water >= self._water_need:self._growth +=self._growth_rate
        
        self._days_growing+=1
        self.update_status()

def auto_grow(crop,days):
    for day in range(days):
        light=random.randint(1,10)
        water=random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
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
            if 1<=water<=10:valid=True
            else:print('not valid')
        except ValueError:
            print('not valid')
    crop.grow(light,water)

def get_menu_choice():
    option_valid=False
    while not option_valid:
            try:
                choice=int(input('Water value?'))
                if 0<=option_valid<=3:valid=True
                else:print('not valid')
            except ValueError:
                print('not valid')
    return choice
def display_menu():
    print('1. manually grow\n2. grow automatically\n3. report status\n0.exit')
    get_menu_choice()

def manage_crop(crop):
    noexit=True
    while noexit:
        display_menu()
        option=get_menu_choice()
        if option==1:manual_grow(crop)
        elif option==2:auto_grow(crop,30)
        elif option==3:print(crop.report())
        elif option==0:noexit=False
        

    
def main():
    new_crop=crop(1,4,3)
    manage_crop(new_crop)

   


if __name__=='__main__':
    main()
