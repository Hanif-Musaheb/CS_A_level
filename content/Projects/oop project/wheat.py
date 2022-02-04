from crop_sim import*
class wheat(crop):
    def __init__(self):
        super().__init__(1,5,5)
        self._type='wheat'
        
    def grow(self,light,water):
        if light>=self._light_need and water>=self._water_need:
            if self._status=='seedling' and water >self._water_need:self._growth+=self._growth_rate*1.5
            elif self._status=='young' and water >self._water_need:self._growth+=self._growth_rate*1.5
            else:self._growth+=self._growth_rate
        self._days_growing+=1
        self.update_status()

def main():
    wheat_crop=wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == '__main__':
    main()
