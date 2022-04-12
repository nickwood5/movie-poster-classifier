#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING cityMap as parameter.
#

def calculateDistance(cityMap):
    city_array = cityMap.split(";")
    city_graph = {}
    
    for row in range (0, len(city_array)):
        for col in range (0, len(city_array[0])):
            tile = city_array[row][col]
            if (tile != "X"):
                if (tile == "T"):
                    target_pos = str(row) + "," + str(col)
                elif (tile == "O"):
                    officer_pos = str(row) + "," + str(col)
                coordinate = str(row) + "," + str(col)
                city_graph[coordinate] = []
                if (col != 0):
                    if (city_array[row][col-1] != "X"):
                        left_coordinate = str(row) + "," + str(col-1)
                        city_graph[coordinate].append(left_coordinate)
                if (col != len(city_array[0])-1):
                    if (city_array[row][col+1] != "X"):
                        right_coordinate = str(row) + "," + str(col+1)
                        city_graph[coordinate].append(right_coordinate)
                if (row != 0):
                    if (city_array[row-1][col] != "X"):
                        above_coordinate = str(row-1) + "," + str(col)
                        city_graph[coordinate].append(above_coordinate)
                if (row != len(city_array)-1):
                    if (city_array[row+1][col] != "X"):
                        below_coordinate = str(row+1) + "," + str(col)
                        city_graph[coordinate].append(below_coordinate)
                
    explored = []
    all_paths = []
    queue = [[officer_pos]]
     
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = city_graph[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == target_pos:
                    all_paths.append(path)
            explored.append(node)   

    smallest_path_length = len(cityMap)
    print(all_paths)
    for path in all_paths:
        if len(path) < smallest_path_length:
            smallest_path_length = len(path)

    return smallest_path_length
            
a = calculateDistance("O__;_XT;___")
print(a)
