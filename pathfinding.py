import random
import math
import sys
import itertools

def pathCost(path, distMat):
	cost = 0
	for i in range(len(path)-1):
		cost += distMat[path[i]][path[i+1]]
	cost += distMat[path[len(path)-1]][path[0]]
	return cost

def genGreedyPath(rankedMat, numnodes):
	path = [0]
	curNode = 0
	visited = set()
	visited.add(0)
	while(len(path) < numnodes):
		for node in rankedMat[curNode]:
			if(node not in visited):
				path.append(node)
				visited.add(node)
				curNode = node
				break		

	path.append(0)
	return path

def genRandomPath(numnodes):
	randpathmid = []
	for i in range(numnodes-1):
		randpathmid.append(i+1)
	random.shuffle(randpathmid)
	randpath = [0]
	randpath.extend(randpathmid)
	randpath.append(0)
	return randpath

def bruteTSP(distMat, numnodes, locs):
	fact = math.factorial(numnodes)
	bestCost = sys.maxsize
	bestPath = []
	randpathmid = []
	for i in range(numnodes-1):
		randpathmid.append(i+1)
	perms = itertools.permutations(randpathmid)
	idx = 1
	for e in perms:
		if idx % 10000 == 0:
			print(1000*(idx/fact), "percent done")
		temppath = [0]
		temppath.extend(list(e))
		temppath.append(0)
		cost = pathCost(temppath, distMat)
		if(cost < bestCost):
			bestCost = cost 
			bestPath = temppath
		idx += 1
	return bestPath