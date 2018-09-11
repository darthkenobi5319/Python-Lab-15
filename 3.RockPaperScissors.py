# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:10:42 2017

@author: ZHENGHAN ZHANG
"""
import random
#the RPS function from Lab 11
def rps(h1,h2):
    choices = ['Rock','Paper','Scissors']
    assert(h1 in choices)
    assert(h2 in choices)
    assignment = {}
    for i in range(len(choices)):
        c = choices[i]
        assignment[c]=i
    n = len(choices)
    outcome =  (assignment[h1]-assignment[h2]+n) % n
    return outcome

class RockPaperScissors:
    def __init__(self):
        self.hand = random.choice(['Rock','Paper','Scissors'])
    def __str__(self):
        return self.hand
    def __gt__(self,opponent):
        a = rps(self.hand,opponent.hand)
        if a == 1:
            return True
        else:
            return False

#main function
while True:
    a=RockPaperScissors()
    b=RockPaperScissors()
    if a>b:
        print('Player 1:',a,'Player 2:',b,' Player 1 wins')
    else:
        if b>a:
            print('Player 1:',a,'Player 2:',b,' Player 2 wins')
        else:
            print('Player 1:',a,'Player 2:',b,' Draw game')
    checker = input('Do you wish to continue?(Y/N)')
    if checker == 'N':
        break