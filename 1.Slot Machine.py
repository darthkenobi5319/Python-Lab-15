# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:13:56 2017

@author: ZHENGHAN ZHANG
"""
import random
class Slot:
    def __init__(self,credit):
        self.credit=credit
    def pull(self,insertion):
        a=random.randint(1,3)
        b=random.randint(1,3)
        c=random.randint(1,3)
        print(a,b,c)
        if a==b==c:
            self.credit += 2*insertion
        else:
            self.credit -= insertion

        
#main program
s = Slot(30)
for i in range(10):
    s.pull(int(input('Enter your coin: ')))
    print('remaining coin',s.credit)