""" Create a sensor network and simulate on it"""

import networkx as nx
import random

# Number of vertices in one row
n = 50
# grid perturbation ratio
pert = 0.4
# udg radius
radius = 0.01
WIDTH = 1.0
HEIGHT = 1.0
N = n * n
STEPX = WIDTH / n
STEPY = HEIGHT / n

# grid perturbed udg network
def getNetwork():
  G = nx.Graph()
  for i in range(n):
    for j in range(n):
      [coorx, coory] = perturb(i, j)
      G.add_node(i*n+j, x = coorx, y = coory)
  for i in range(N):
    for j in range(N):
	  if (euDist2(G, i, j) <= radius * radius):
	    G.add_edge(i, j)
  return G

def euDist2(G, i, j):
  x1 = G.node[i]['x']
  y1 = G.node[i]['y']
  x2 = G.node[j]['x']
  y2 = G.node[j]['x']
  return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)
  
# Generate the coordinate for node with index i*n+j
def perturb(i, j):
  x = STEPX/2 + i*STEPX
  y = STEPY/2 + j*STEPY
  signX = random.randint(0,1)*2 - 1
  signY = random.randint(0,1)*2 - 1
  jumpX = random.random()*STEPX*pert
  jumpY = random.random()*STEPY*pert
  x = boundX(x+signX*jumpX, 0, WIDTH)
  y = boundY(y+signY*jumpY, 0, HEIGHT)
  return [x,y]

def boundX(x, left, right):
  if x < left:
    return left
  if x > right:
    return right
  return x

def boundY(y, top, bottom):
  if y < top:
    return top
  if y > bottom:
    return bottom
  return y

if __name__ == "__main__":
  G = getNetwork()
  print G.order()
  print G.node[1]['x']
