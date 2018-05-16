'''
Created on 15 May 2018

@author: mark
'''
class C(object):
    'some doxs'
    
    a = 10
    
    def __init__(self, x=1):
        self.x = x
        
    def showx(self):
        print self.x
        
o = C()
o2 = C(3)
o.x += 1
o.showx()
o2.showx()