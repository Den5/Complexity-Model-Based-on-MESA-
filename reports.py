# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:52:00 2018

@author: dsutherland
"""

def assignments (model):
    agents_per_pool = []
    
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        agents_per_pool.append(agent_count)
        print('Agents per Pool' ,agent_count) ### aded to show values
       
    return agents_per_pool



def total_wealth(model):
    #agent_wealths funtion to add up each agent model through all models
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    total_wealth = sum(agent_wealths)
    return total_wealth       




def model_wealth(model):
    # #calculate model per model data 
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    model_wealth = sum(agent_wealths)
    return model_wealth


def deg (self):
    assignments = self.datacollector.get_model_vars_dataframe()
        #assignments = assignments['Assignment']
    last = assignments['Assignment'].iloc[-1]
        #print (assignments)
    print (last, 'Last')
    return