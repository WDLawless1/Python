# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 07:31:52 2020

@author: user
"""

import math
a = float(input("Please enter the length of the opposite side (in meters): "))
b = float(input("Please enter the length of the adjacent side (in meters): "))
c = math.sqrt(a**2 + b**2)
alpha = math.degrees(math.atan(a/b))
print('The hypotenuse of this right triangle is ', c, 'meters. and the angle is', alpha,' degrees.')
