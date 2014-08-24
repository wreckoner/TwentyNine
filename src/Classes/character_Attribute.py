'''
Created on Jul 25, 2014

@author: Dip
'''
from string import count
from lib2to3.fixer_util import String
import math
from random import random, randint
""" 
 1.hand_strength

 2.aggression

 3.defense

 4.double

 5.partner

 6.pair
 
 7.set_condition
 
""" 

class hand_analyser():
    
    def __init__(self,hand,index):
        self.hand = hand
        self.index=index
#     
#     initial_value=15   # dak suru hoy 16 theke
#     
#     player_name='kesto' # ata computer randomly player select kore tar name ta pathabe.
#     
#     hand=[['J','hearts'],['K','hearts'],['A','spade'],['10','diamond']]  # player er hand ta pathabe computer
#     
#     partner_bid=0  # partner bid koreche kina, na kore thakle value 0,kore thakle joto abdhi dekeche tato ta
#     
    cons= {'A': 1.5,
            'K': 0.5, 
            'Q': 0.5,
            'J': 4,
           '10': 1,
            '9': 2, 
            '8': 0.5,
            '7': 0.5}
 
    point_calculation=0
#     
#     
    def hand_strength(self):
        suit=[]
        calculation=0
        trump_order=[]
        trump=''
        print self.index
        for i in range(4):
            suit.append(str(self.hand[i]).split(' - '))
        print suit
#          print sum(x.count(suit[0][0]) for x in suit)
#          print hand_analyser.cons[suit[0][1]]
        for i in range(4):
#              print (hand_analyser.cons[suit[i][1]]*sum(x.count(suit[i][0]) for x in suit))
            calculation+=(hand_analyser.cons[suit[i][1]]*sum(x.count(suit[i][0]) for x in suit))
            trump_order.append([sum(x.count(suit[i][0]) for x in suit),hand_analyser.cons[suit[i][1]]])
        trump_order.sort()
        for i in range(4):
            if trump_order[3][0]==sum(x.count(suit[i][0]) for x in suit) and trump_order[3][1]== hand_analyser.cons[suit[i][1]] :
                trump=suit[i][0]
                print trump
                break
#          print calculation
#          print(15+int(round(calculation/2.615)))
        final_bid=15+int(round(calculation/2.615))
        
        result=[final_bid,trump] 
        print result
        print '------------------------------k'
        return result
    
    
    def aggression(self):
        
        return randint(-2,2)
    
    
    
    def double(self):
        chances_of_double=[0,0,0,0,0,0,0,0]
        suit=[]
        for i in range(4):
            suit.append(str(self.hand[i]).split(' - '))
        if sum(x.count('J') for x in suit)==2:
            chances_of_double=[1,1,1,1,1,0,0,0]
            reduction=-1
        if sum(x.count('J') for x in suit)==3:
            chances_of_double=[1,1,1,1,1,1,1,0]
            reduction=-1
        
        
        return 0   


    def set_condition(self):
        return 0


    def partner_call(self):
        return 0
    
    
    
    def pair(self):
        return 0
    

        
    
#    point_calculation+=hand_strength() + aggression() + defense() + double() + partner_call() + pair()
 
