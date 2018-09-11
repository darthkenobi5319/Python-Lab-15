# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:38:55 2017

@author: ZHENGHAN ZHANG
"""
import time

class QuestionAnswer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def ask(self):
        print(self.question)
        return input('Your Answer:')

class Timer:
    def __init__(self):
        self.watches=[]
        self.begin=0
    def start(self):
        self.begin=time.time()
    def stop(self):
        self.watches.append(time.time()-self.begin)
    def results(self):
        print(self.watches)
        m=0
        for i in self.watches:
            m+=i
        avg=m/len(self.watches)
        print('Average Time:',avg)

#main program
QA=[]
QA.append(QuestionAnswer('Who is the greatest singer in the world?','Taylor Swift'))
QA.append(QuestionAnswer('Which is the worse Game Company in the United States?','EA'))
QA.append(QuestionAnswer('Which is the worse Game Company in the World?','Ubisoft'))
QA.append(QuestionAnswer('Which is the worse Game Company in the Canada?','Ubisoft Montreal'))
t=Timer()
for i in range(len(QA)):
    t.start()
    while True:
        a=QA[i].ask()
        if a == QA[i].answer:
            break
    t.stop()
t.results()
    