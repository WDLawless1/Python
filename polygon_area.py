# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 02:35:53 2020

@author: user
"""

from math import tan, pi
side = int(input('Please enter the number of sides (n >= 3): '))
length = float(input('Please enter the length of each side (in meters) : '))
area = side * (length ** 2) / (4 * tan(pi  /side))
print('The area of this ', side, '-sided polygon is ', area,' square meters.')
