'''
Created on 16 May 2018

@author: mark
'''
import logging as log
try:
    'mess'
    log[0]
    #a
    #1/0
except ZeroDivisionError:
    print "cannot div bt 0"
except NameError:
    print "name not defined"
except Exception as e:
    log.exception(e)
else:
    print "no exception"
finally:
    print "we do this no matter what"
    
    
while True:
    try:
        int(raw_input("Enter an int: "))
    except ValueError:
        print "not a number"
    else: break
   
    
    
    

