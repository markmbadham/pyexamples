'''
Created on 15 May 2018

@author: mark
'''
def greeter(name, surname=''):
    'greeter function'
    return 'hello {} {}'.format(name, surname)
    
def square(x, y=2):
    return x ** y

def tree(n=5):
    out = []
    for i in range(1,n+1):
        out.append(('* '*i).center(n*2))
    return '\n'.join(out)

def factorial(n):
    out = 1
    for i in range(1,n+1):
        out *= i
    return out

def factorial1(n):
    out = n
    for i in range(n-1,0,-1):
        out *= i
    return out

def factorialr(n):
    if n>1:
        return n * factorialr(n-1)
    else:
        return 1

def factorialr1(n):
    return n * factorialr(n-1) if n>1 else 1

def make_double(fn):
    def inner(*args, **kwargs):
        return 2*fn(*args, **kwargs)
    return inner

@make_double
def cube(x):
    return x**3
#cube = make_double(cube)

def show_args(*args, **kwargs):
    print args, kwargs

@make_double    
def my_sum(*args):
    'the too easy way'
    return sum(args)

def my_sum1(*args):
    out = 0
    for i in args: out += i
    return i

def avg(*args):
    return my_sum(*args)/len(args)

def get_num(num_type, message="Enter a number: "):
    while True:
        try:
           i = num_type(raw_input(message))
        except ValueError:
            print "not a number"
        else:
            return i
        
def get_int(message):
    return get_num(int, message)    

def get_float(message):
    return get_num(float, message)

if __name__ == '__main__':
   i = get_num(int)






