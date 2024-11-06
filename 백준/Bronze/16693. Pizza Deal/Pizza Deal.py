import sys
from math import pi
# 경우 1: price p1 + area a1
# 경우 2: price p2 + radius r1

# maximize the amount of pizza you get Dollar

# INPUT
# First Line: a1 p1
# Second Line: r1 p2
a1, p1 = map(int, sys.stdin.readline().split())
r1, p2 = map(int, sys.stdin.readline().split())



# LOGIC
pizza_per_area = a1/p1
pizza_per_radius = ((r1**2)*pi)/p2

# print(pizza_per_area)
# print(pizza_per_radius)

# OUTPUT: better deal 
if pizza_per_area >= pizza_per_radius:
    print("Slice of pizza")

if pizza_per_radius >pizza_per_area:
    print("Whole pizza")