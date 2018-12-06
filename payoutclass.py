# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:15:53 2018

@author: dsutherland
"""

#from model import *
import numpy as np 

#inputs agent assignments and works out the payments for the three pools

class Payout():
    
    #An Agent with fixed intial wealth
    def __init__(self, assignments):
        super().__init__()

        self.assignments = assignments
    

        
    def low(self, assignments):
        if assignments==0: 
            return 0
        
        prob = 5
        value = 40 / assignments
        if np.random.randint(0,9) >= prob:
            value = 0    
        return int(value)

    def stable(self, assignments):
        if assignments==0: 
            return 0
        prob = 1
        value = 1
        return prob * value
    
    def high (self, assignments):
        if assignments==0: 
            return 0
        prob = 25
        value = 80 / assignments
        if np.random.randint(0,99) >= prob:
            value = 0
        return int(value)

 

    def pay_out(self):
    #taking a list assignments and using the functions to work out the payouts per pool
    
    
        num_low = self.assignments[0]
        num_stable = self.assignments[1]
        num_high = self.assignments[2]
    
        low_pay = self.low(num_low)
        stable_pay = self.stable(num_stable)
        high_pay = self.high(num_high)
        
        return [low_pay, stable_pay, high_pay]
  
        

 
