# Loads and calls a c library function
# Run using: python arrayuse.py

import numpy as np
from numpy import ctypeslib
from ctypes import *
import math
import multiprocessing

# Loads the c library
arraytest = cdll.LoadLibrary('./doWork.so.1.0')
# Provides a python function prototype for the c library function
arraytest.runsim.argtypes = [c_double, c_double, c_double, c_double, c_double]
# This is a wrapper function for the c library function
def runsim(k):
    #Call the library function
    arraytest.runsim(k[i][0], k[i][1], k[i][2], k[i][3], k[i][4])

# Create a kvector - actually nonsense
k = np.ndarray(shape=(27,5), dtype=np.double)
#k = np.array([0.0, 0.0, 0.0, 20000, 0.0])

# Test the function
k[0] = np.array([0.0, 0.0, 0.0, 50000, 0.0])

print k[0]
a = (0.5)
GammaX = 2*math.pi/(a*math.sqrt(3))
k[0][0] = -GammaX/2
k[0][1] = GammaX*math.sqrt(3)/2
step = GammaX/10


for i in range(1,10):
    k[i][0] = k[i-1][0] - step/2
    k[i][1] = k[i-1][1] + step*math.sqrt(3)/2
    k[i][2] = k[i-1][2]
    k[i][3] = k[i-1][3]
    k[i][4] = k[i-1][4] + 1.0

GammaJ = 2*GammaX/math.sqrt(3)
step = GammaJ/10

for i in range (10, 21):
    k[i][0] = k[i-1][0] 
    k[i][1] = k[i-1][1] + step
    k[i][2] = k[i-1][2]
    k[i][3] = k[i-1][3]
    k[i][4] = k[i-1][4] + 1.0

XJ = GammaX/math.sqrt(3)
step = XJ/5

for i in range (21, 26):
    k[i][0] = k[i-1][0] - step/2
    k[i][1] = k[i-1][1] - step*math.sqrt(3)/2
    k[i][2] = k[i-1][2]
    k[i][3] = k[i-1][3]
    k[i][4] = k[i-1][4] + 1.0
    

for i in range (19, 26):
    p = "p%d" %i
    print p
    p = multiprocessing.Process(target = runsim, args =(k,))
    print i
    print k[i]
    p.start()
    #p.join()
print "Done"

