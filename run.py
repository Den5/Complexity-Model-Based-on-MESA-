# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:48:00 2018

@author: dsutherland
"""

from model import *
import matplotlib.pyplot as plt 
               
    #run the model
model = MModel(20,3,1)
#model = MModel(10,5,5)    



for i in range(15):
    model.step()
    
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        #print('Agents per cell' ,agent_count) ### aded to show values
        agent_counts[x][y] = agent_count
    plt.imshow(agent_counts, interpolation='nearest')
    plt.colorbar()
    plt.show()



#agent level graphs / although all agents
# Panads DF of agent wealth per model
agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.plot.bar()

#single agent
agent = 10
one_agent_wealth = agent_wealth.xs(agent, level='AgentID')
one_agent_wealth.plot(title= str(agent))

#create a list of agent level wealth
agent_wealths = [agent.wealth for agent in model.schedule.agents]
print (agent_wealths)

#model level graphic
model_wealth = model.datacollector.get_model_vars_dataframe()
model_wealth.plot()







#b= model.datacollector.get_agent_vars_dataframe()  
#print(b, 'This is the full dataframe')