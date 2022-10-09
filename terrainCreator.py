from re import A
import numpy as np
from numpy import random
import csv

def creatMap():
    
    map = random.randint(1, size=(1000,1000))
    #for i in range(1000):
     #   for j in range(1000):
      #      map[i][j]=random.randint(1,3)
    
    with open("map.csv","w",newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(map)
    
    return map

