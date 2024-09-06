#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: yangyangwang
"""

import random #imports built-in module
import math #imports built-in module

# function for simulating a world series
def worldseries(p, N): #defines worldseries function
    """
    Function for simulating a world series
    p is the probability that the best team wins
    N is the number of games in the world series , usually take N=7
    """
    win = 0 #value for win starting at 0
    lose = 0 #value for lose starting at 0
    while (max(win, lose) < math.floor(N/2)+1): 
        if random.random() < p: #if the random generator generates a value under .65
            win = win + 1 #add to win tally
        else :
            lose = lose +1 #otherwise, add to loss tally
    return win, lose #return randomly generated win and loss tally