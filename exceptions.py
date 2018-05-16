#! /usr/bin/env python
import traceback as tb
import logging as log
FORMAT = '%(asctime)s:%(levelname)10s:%(message)s'
log.basicConfig(format=FORMAT,
        filename='logger.log', 
        level=log.DEBUG)
logger = log.getLogger(__name__)

x = 'abc'
try :
    log.debug('starting try block')
    assert False, "force exception"
    x[4]
    1/0
    print a

except ZeroDivisionError:
    log.error("can't devide by zero")
except NameError:
    print "name not defined"
except IndexError:
    print "index out of range"
except:
    print "other error"
    log.error("some other exception occured")
    log.error(tb.format_exc())
else:
    print "no exception occured"
finally:
    print "we do this no matter what"
