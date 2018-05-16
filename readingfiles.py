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

def read_config1(key):
    with open('../../config.text') as f:
        for line in f:
            if line.startswith(key):
                return line.split('=')[1].strip()

def read_config(filename):
    d = {}
    with open(filename) as f:
        for line in f:
            try:
                key, val = line.split('=')
                d[key.strip()] = val.strip()
            except ValueError:
                pass
    return d
if __name__ == '__main__':
    print read_config('../../config.text')