from animal import*

class cow(animal):
    def __init__(self,name):
        super().__init__(1,3,6,'cow1')
        self._type='cow'
        
    def grow(self,food,water):
        if light>=self._food_need and water>=self._water_need:
            if self._status=='baby' and water >self._water_need:self._growth+=self._growth_rate*1.5
            elif self._status=='very young' and water >self._water_need:self._growth+=self._growth_rate*1.5
            else:self._growth+=self._growth_rate
        self._days_growing+=1
        self.update_status()
        
