import random 
import math
import numpy as np
import itertools
import sys
from visualize import plotTSP
import threading
from pathfinding import pathCost, genGreedyPath, genRandomPath, bruteTSP

MAXY = 10
MAXY = 10
NUMTHREADS = 4
numnodes = 10


locs = []

for i in range(numnodes):
	y = random.randint(0, MAXY)
	x = random.randint(0, MAXY)
	locs.append([x,y])

print(locs)

distMat = np.zeros([numnodes, numnodes])
for i in range(numnodes):
	for j in range(numnodes):
		if(i != j):
			distMat[i][j] = math.sqrt((locs[i][0] - locs[j][0])**2 + (locs[i][1] - locs[j][1])**2)

print(distMat)

rankedMat = []
for row in distMat:
	rowRank = {}
	for idx, e in enumerate(row):
		rowRank[idx] = e
	reRank = {k: v for k, v in sorted(rowRank.items(), key=lambda item: item[1])}
	newRank  = list(reRank.keys())
	newRank.pop(0)
	rankedMat.append(newRank)

print(rankedMat)

path = genGreedyPath(rankedMat, numnodes)
print(path)
print(pathCost(path, distMat))


randpath = genRandomPath(numnodes)
print(randpath)
print(pathCost(randpath, distMat))


bestpath = bruteTSP(distMat, numnodes, locs)
print(bestpath)
print(pathCost(bestpath, distMat))
plotTSP(bestpath, locs, 1)
