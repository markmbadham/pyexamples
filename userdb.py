'''
Created on 18 May 2018

@author: mark
'''
import sqlite3 as db     
                                      
class UserDb(object):
    def __init__(self, constring='test.db'):
        self.con = db.connect(constring)                                    
        self.cur = self.con.cursor()
    
    def create_table(self):
        'create a string with sql create table code'
        
        sql = '''CREATE TABLE users(                                   
                    id INT PRIMARY KEY,  
                   username VARCHAR(64),  
                    password VARCHAR(64))'''
        #execute the sql code
        self.cur.execute(sql)
        return self
        
    def add_users(self, *args):
        sql = '''INSERT INTO users
                 VALUES(?, ?, ?)''' 
        if type(args[0]) in (tuple, list): 
            self.cur.executemany(sql,args)
        else:
            self.cur.execute(sql,args)
        self.con.commit()
        return self
   
    def show_table(self):
        sql = 'SELECT * FROM users'
        print self.cur.execute(sql).fetchall()

if __name__ == '__main__':
    UserDb().add_users(10,'max','imus').show_table()
