# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:43:55 2018

@author: dsutherland
"""

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from model import MModel


def agent_portrayal(agent):
    portrayal = {'Shape' : 'circle',
                 'Color' : 'red',
                 'Filled': 'true',
                 'Layer' : 0,
                 'r' : 0.1}
    
    return portrayal

grid = CanvasGrid(agent_portrayal, 3, 1, 500, 500)




chart = ChartModule([{"Label": "Total_Wealth_All_Models",
                      "Color": "Black"}],
                    data_collector_name='datacollector')
 
n_slider = UserSettableParameter('slider', "Number of Agents", 10, 2, 20, 1)
    
server = ModularServer(MModel,
                       [grid, chart],
                       "The Model",
                       {"N" : n_slider, "width": 3, "height" : 1})

server.port = 8541 # The default
server.launch()

