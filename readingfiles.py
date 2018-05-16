'''
Created on 16 May 2018

@author: mark
'''
import os

def readfile(dirname):
    print dirname
    if os.path.isdir(dirname):
        for filename in os.listdir(dirname):
             readfile(dirname+'/'+filename)

def readfile2(dirname, indent=0):
    print indent*'  ' + dirname
    if os.path.isdir(dirname):
        oldir = os.path.abspath('.')
        os.chdir(dirname)
        for filename in os.listdir('.'):
             readfile2(filename, indent + 1)
        os.chdir(oldir)
        

if __name__ == '__main__':
    readfile2('/home/mark/Documents/course/python')