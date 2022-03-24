# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:36:57 2022

@author: Admin
"""

from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range (180):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)
done()