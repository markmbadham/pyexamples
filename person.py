'''
Created on 15 May 2018

@author: mark
'''
class Person(object):
    
    def __init__(self, name='', age=0):
       
        self.name = name
        self.age = age
    
    def talk(self):
        return 'hello my name is {}'.format(self.name)
    
    def walk(self):
        age = self.age
        if age <= 1:
            return "Crawl - 4 legs"
        elif age <= 75:
            return "walk - 2 legs"
        else:
            return "Hobble - 3 legs"
        
    def set_name(self, val):
            self.fname, self.surname = val.split()
    def get_name(self):
            return  self.fname + ' ' + self.surname
    name = property(get_name, set_name)
    
    def __str__(self):
        return "Person {} {} ".format(self.name, self.age)
    
    def __repr__(self):
        return "Person(name={}, age={})".format(self.name, self.age)
    
class Employee(Person):
        
    def __init__(self, name='', age=0, job=''):
        Person.__init__(self, name, age)
        self.job = job
    
    def work(self):
        return 'i am doing {}'.format(self.job) 
       
fred = Person('Fred Blogs')
print repr(fred)
str()


        