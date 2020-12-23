import numpy as np
import math
import matplotlib.pyplot as plt


def trial(dimension):
    grid = np.zeros(int(math.pow(2*dimension,2)), dtype=int).reshape(2*dimension, 2*dimension)
    grid[0] = np.arange(-dimension, dimension)
    grid[:, 0] = np.arange(-dimension, dimension)
    for i in range(1, len(grid)):
        a = abs(grid[0][i])
        for j in range(1, len(grid[0])):
            b = abs(grid[j][0])
            if a >= b:
                grid[i][j] = abs(a +  b)
            else:
                grid[i][j] = abs(b + a)
    print(grid)
    grid = np.delete(grid, 0, 0)
    grid = np.delete(grid, 0, 1)
    grid = np.delete(grid, dimension,0)
    grid = np.delete(grid, dimension, 1)
    plt.imshow(grid)
    plt.show()

def main(dimension):
    grid = np.zeros(int(math.pow(dimension, 2)), dtype=int).reshape(dimension, dimension)

    grid[0] = np.arange(dimension)
    grid[:, 0] = np.arange(dimension)

    for i in range(1, len(grid)):
        a = grid[0][i]
        for j in range(1, len(grid[0])):
            b = grid[j][0]
            if a >= b:
                grid[i][j] = a%b*60
            else:
                grid[i][j] = b%a*60

    g0 = np.delete(grid, 0,0)
    g1 = np.delete(g0, 0, 1)

    plt.imshow(g1)
    plt.show()

trial(100)
