
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:37:04 2018

@author: dsutherland
"""

#from model import *
import numpy as np
import pandas as pd

# defines strtegy for the agents to move around
# create a DF with the following format




class Strategy():
    
    #An Agent with fixed intial wealth
    def __init__(self):
        pass
 
    print ('ok')
    #strategty to move agents randomly
    def rand_pos(self):
        self.bit = np.random.randint(1,4)
        self.new_position = (self.bit,0)  
    
        return self.new_position

    
    
    


