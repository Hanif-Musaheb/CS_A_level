from crop_sim import*
class potato(crop):
    def __init__(self):
        super().__init__(1,3,6)
        self._type='potato'
        
    def grow(self,light,water):
        if light>=self._light_need and water>=self._water_need:
            if self._status=='seedling' and water >self._water_need:self._growth+=self._growth_rate*1.5
            elif self._status=='young' and water >self._water_need:self._growth+=self._growth_rate*1.5
            else:self._growth+=self._growth_rate
        self._days_growing+=1
        self.update_status()

def main():
    potato_crop=potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == '__main__':
    main()
