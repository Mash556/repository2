class Auto:
    def ride(self):
        print('Riding on a ground')
    
class Boat:
    def swim(self):
        print('Floating on water')
    
class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim() 