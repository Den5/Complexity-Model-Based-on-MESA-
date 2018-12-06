# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:27:20 2018

@author: dsutherland
"""

# This is the Complexity Challenge - Sping 2018

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from strategy import *
from payoutclass import Payout
import random
import pandas as pd
from reports import *

class MAgent(Agent):
    
    #An Agent with fixed intial wealth
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.xy = (0,0)
        self.strategy = Strategy()
       
    """
    def select_strategy(self):
        #create an agent per move strategy
        self.strategy = Strategy()
        #selects an agent strategy
        self.xy = self.strategy.rand_pos()
        return self.xy
        """
  

    def move(self):
        # move agent next tick
        #self.select_strategy()
        self.xy = self.strategy.rand_pos()
        return self.model.grid.move_agent(self, self.xy)
    
            
    def step(self):
        #agents step goes here
        self.move()        
        #Console readout
        print ('I am Agent' , self.unique_id , 'and I am here:', self.xy, 'worth', self.wealth)    
        
        
       


class MModel(Model):
    #A model with some number of agents
    # Inherits 'Model' from Mesa, and 'Location' from other class
    #this allow instances of this class to run the 'Location' methods
    def __init__ (self, N, width, height):
        super().__init__()
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
 
          # create the agents
        for i in range(self.num_agents):
            a = MAgent(i, self)
            self.schedule.add(a)
                      
            # add agents to random point on grid
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            print('place agent in pos', a.pos)
            
         
            #collect data for charts
            self.datacollector = DataCollector(
                    agent_reporters={"Wealth": "wealth","Location": "xy"},  # An agent level stat collector
                    model_reporters={'Total_Wealth_All_Models': total_wealth, 'Assignment': assignments})  # model level stat collector
   
    


    
    def pay(self):
        
        # obtain the amounts of agents per pool, work out how much they are paid  
        #then assign new $$ to them based on the pool they are in
        
        model_wealth = self.datacollector.get_model_vars_dataframe()
        assign = model_wealth['Assignment'].iloc[-1]
        #print ( 'There are the numbers of agents per poll', assign)
        
        p = Payout(assign)
        self.pay_list = p.pay_out()
        #print ( 'The is amount agents receive on a per pool Payout', self.pay_list)
        
        for agent in self.schedule.agents:
            #print (agent.unique_id, agent.wealth, agent.pos  , 'agents stats')
  
            if agent.pos == (1,0):    
        #Low Pool
                agent.wealth = agent.wealth + self.pay_list[0]
           
    
            if agent.xy == (2,0):
        #Stable Pool
                agent.wealth = agent.wealth + self.pay_list[1]
         
    
            if agent.xy == (3,0):
        #high
                agent.wealth = agent.wealth + self.pay_list[2]
      
        return
                        



    def step(self):
        #advance the model by one step
        self.datacollector.collect(self)
        self.schedule.step()
        self.pay()
        
        #calculate model per model data  each step
        print ('Model Wealth =', model_wealth(self))
        

        

   
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    