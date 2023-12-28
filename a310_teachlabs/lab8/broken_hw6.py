import numpy as np 
import math
import matplotlib.collections as mc 
import matplotlib.pylab as pl

random_seed = 1729 
np.random.seed(random_seed)
N = 40 
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x,y)
cities = list(points)

itinerary = list(range(0,N))
# traveling order 
 

def findnearest(cities, index, nnitinerary):
    '''
    finds the nearest neighbor of a given city (index) provided with a list of cities 
    cities = all cities 
    index = current position
    nnitinerary = current itinerary up to the point of iteration     
    '''
    mindex = -1
    point = cities[index]
    mindistance = float('inf')
    for i in range(0, len(cities)):
        distance = math.sqrt((point[0]- cities[i][0])**2 + (point[1] - cities[i][1])**2)
        if distance < mindistance and distance > 0 and i not in nnitinerary:
            mindistance = distance 
            mindex = i
    return mindex 

def donn(cities, N):
    '''
    implementation of the nearest neighbor algorithm. 
    iterates over all the cities
    '''
    nnitinerary = [0]
    for i in range(0, N-1):
        next = findnearest(cities, nnitinerary[len(nnitinerary)-1], nnitinerary)
        nnitinerary.append(next)
        return (nnitinerary)







# code for the visualization - not for algo. 


def genlines(cities, itinerary):
    lines = []
    for city in range(0, len(itinerary)-1):
        lines.append([cities[itinerary[city]], cities[itinerary[city+1]]])
    return (lines)

# the salesman lives on a flat earth 
# ie, use pythagorean to compute distance

def howfar(lines):
    distance = 0 
    for j in range(0, len(lines)):
        distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0])**2 +  
                              abs(lines[j][1][1] - lines[j][0][1])**2)
    return distance



 
def plotitinerary(cities, itin, plottitle, thename):
    lc = mc.LineCollection(genlines(cities, itin), linewidths = 2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x,y)
    pl.title(plottitle)
    pl.xlabel('X coordinate')
    pl.ylabel('Y coordinate')
    pl.savefig(str(thename) + '.png')
    pl.close()


plotitinerary(cities,donn(cities,N),'TSP - NearestNeighbor','nearest_neighbor')
print(howfar(genlines(cities,donn(cities,N))))