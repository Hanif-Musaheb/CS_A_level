from potato import*
from wheat import*
from sheep import*
from cow import*

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
        

def main():
    new_field= field(5,2)
    print(new_field._crops,new_field._animals,new_field._max_animals,new_field._max_crops)
    new_field.plant_crop(wheat())
    new_field.add_animal(sheep('cow1'))
    print(new_field._crops)
    print(new_field._animals)
    new_field.harvest_crop(0)
    new_field.remove_animal(0)
    print(new_field._crops)
    print(new_field._animals)
    
if __name__=='__main__':
    main()
