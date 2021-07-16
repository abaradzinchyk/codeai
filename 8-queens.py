#!/usr/bin/env python2
# # -*- coding: utf-8 -*-
""" 8-queens.py """
__author__="Alexander_Baradzinchyk"

        
desk_size = 8
queen_location = []

# example of queen_location = [[1[8, 2, 5, 1, 3, 4, 7, 6]]



def place_queen(x, y):
    if 1 <= x <= desk_size and 1 <= y <= desk_size:
        if not [x, y] in queen_location:
            queen_location.append([x, y])
            print('Queens placed:', len(queen_location), 'from:', desk_size, '\nQueens coordinates:', queen_location)


while len(queen_location) != desk_size:
    place_queen(*[int(x) for x in (input('\nPlace the queen at location X and Y\nUse space between X and Y\nlike 1 5:\n').split())])


print('No') if sum([len(x) for x in (list(map(set, zip(*[(x, y, y + x, y - x) for x, y in queen_location]))))]) != desk_size * 4 else print('Yes')