# -*- coding: utf-8 -*-
"""

Justin Berg
Akhil Kumar Reddy Gopireddy
Tyler C. O'Brien
IE 8030 Final Project Model
Dr.Emily Tucker
4/26/21

"""
# Set up packages
from pyomo.environ import *

# Set 1 (Set of API sites)
S = {"USA", "Mexico", "Puerto Rico", "Ireland", "Italy", "Hungary", "Croatia", "Israel", "India", "China"}
print(S)

# Set 2 (Set of Manufacturing Sites)
F = {"USA", "Mexico", "Puerto Rico", "Ireland", "Italy", "Hungary", "Croatia", "Israel", "India", "Canada", "Venezuela", "Peru", "Chile", "Brazil", "Argentina", "Iceland", "Netherlands", "Spain", "UK", "Poland", "Italy", "Germany", "Malta", "Lithuania", "Russia", "Serbia", "Czech", "Hungary", "Romania", "Bulgaria", "Greece", "Japan", "Thailand", "Singapore", "Indonesia"}
print(F)
# Variables
# Amount Sent from API Site (in set S) to Manufacturing Site (in set F)
