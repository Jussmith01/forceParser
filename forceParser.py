#!/usr/bin/python

import numpy as np

def solve(lis):                                        
    for x in lis:
        try:
            yield float(x)
        except ValueError:    
            pass

print("Hello, Python!")

filename = "trainingData.dat"

fvalues = np.zeros(shape=(2,4))
i = 0
with open(filename,'r') as f:
    for line in f:
        svalues = line.split(",")
        tmpval = solve(svalues)
        tlist = []
        for v in tmpval:
            tlist.append(v)
        fvalues[i]=tlist
        i=i+1 
 
print(fvalues)
