'''
Created on 15 May 2018

@author: mark
'''
from jedi.debug import speed

class Car(object):
    '''
    car class
    '''
    power = 5

    def __init__(self, speed=0, heading=0):
        '''
        Constructor
        '''
        self.speed = speed
        self.heading = heading
    @classmethod
    def get_power(cls):
        return cls.power
    
    def turn(self, angle):
        self.heading = (self.heading + angle) % 360
        if self.heading < 0:
            self.heading = 360-self.heading 
        
    def accelerate(self):
        self.speed += self.get_power()
        
def show_car(car):
    print "heading", car.heading
    print "speed", car.speed

class SportsCar(Car):
    power = 10
    
    def __init__(self, speed=0, heading=0, spoiler=False):
        Car.__init__(self, speed, heading)
        self.spoiler = spoiler
        
    def donut(self):
        return "screech"
    
    def race(self):
        return "racing"

if __name__ == '__main__':
    my_car = SportsCar()
    your_car = Car()
    your_car.accelerate()
    my_car.accelerate()
    my_car.turn(45)
    show_car(my_car)
    show_car(your_car)
    print isinstance(my_car, SportsCar)
    print type(my_car)
    print my_car.donut()
    
    
    