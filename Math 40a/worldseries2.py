#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: yangyangwang
"""

import random
import math
def worldseries(p, N):
      '''
      Function for simulating a world series
      p is the probability that the best team wins
      N is the number of games in the world series, usually take N=7
      '''
      win = 0
      lose = 0
      while (max(win,lose) < math.floor(N/2)+1):
          p_real = p + 0.05*random.random()
          if random.random() < p_real:
              win = win + 1
          else:
              lose = lose + 1
      return win, lose