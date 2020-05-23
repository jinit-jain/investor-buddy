# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:12:24 2020

@author: siddh
"""

from csv import reader

from plot_map import plot_map

DIR = 'csv/'

x_points = []

with open('{}xPoints.csv'.format(DIR), 'r', encoding='utf-8') as temp:
    t1 = reader(temp)
    for value in t1:
        x_points.append(float(value[0]))
        # print(beta[-1])
        
plot_map(x_points)