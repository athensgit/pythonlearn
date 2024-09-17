#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: yangyangwang
"""

import random #imports built-in module
import math #imports built-in module
def worldseries(p, N):
      '''
      Function for simulating a world series
      p is the probability that the best team wins
      N is the number of games in the world series, usually take N=7
      '''
      win = 0 #value for win starts at 0
      lose = 0 #value for win starts at 0
      while (max(win,lose) < math.floor(N/2)+1): #loop that stops once one team wins/loses 4 games out of 7)
          p_real = p + 0.05*random.random() 
          '''defines new probability that equals inputted probability with an 
          added random increment of probability resulting in a p between p and p + 0.05. Introduces element of variation'''
          if random.random() < p_real: #if the random generator generates a value under the new probability
            win = win + 1 #add to win tally
          else:
            lose = lose + 1 #otherwise, add to loss tally
      return win, lose #return randomly generated win and loss tally