'''
Created on 16 May 2018

@author: mark
'''
from readingfiles import read_config

FILENAME = '../../config.text'

class Config(object):
    '''
    Reads a config file in INI format
    And provides methods to get and set the parameters
    '''
    def __init__(self, filename=FILENAME):
        '''
        Constructor
        '''
        self.filename = filename
        self.read()
        
    def read(self):
        self.data = read_config(self.filename)
        
    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, val):
        self.data[key] = val


if __name__ == '__main__':
    config = Config()
    print config.get('port')

        
        
        