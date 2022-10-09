import numpy as np
import random

def creatMap():
    map = np.zeros((1000,1000))
    for i in range(1000):
        for j in range(1000):
            map[i][j]=random.randint(1,5)
    return map

