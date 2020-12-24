import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

FULL = 255
EMPTY = 0

def countNeighbors(m, row, col):
    count = int(m[row-1][col-1] + m[row-1][col] + m[row-1][col+1] + m[row][col-1] + m[row][col+1] + m[row+1][col-1]
                + m[row+1][col] + m[row+1][col+1])//255
    return count

def roundOfGame(m):
    m_update = m.copy()
    for i in range(1,99):
        for j in range(1,99):
            num_neighbors = countNeighbors(m, i, j)
            if m[i][j] == FULL:
                if num_neighbors < 2 or num_neighbors >3:
                    m_update[i][j] = EMPTY
            else:
                if num_neighbors == 3:
                    m_update[i][j] = FULL

    return m_update

def initializeGlider(m, i, j):
    m[i][j] = 255
    m[i][j+2] = 255
    m[i+1][j+1] = 255
    m[i+1][j+2] = 255
    m[i+2][j+1] = 255

def initializeRandom(m):

    for i in range(1,99):
        for j in range(1,99):
            a = random.randint(1,7)
            if a>6:
                m[i,j] = 255


def updatefig(j):
    im.set_array(sequence[j])
    return [im]



##################### main()
m = np.zeros((100,100), dtype = int)

# initialize glider
# initializeGlider(m, 10, 50)
initializeRandom(m)

sequence = []
sequence.append(m)
for i in range(100):
    m_current = roundOfGame(m)
    sequence.append(m_current)
    m = m_current


fig = plt.figure()
im = plt.imshow(sequence[0], cmap = plt.get_cmap('jet'), vmin = 0, vmax = 255)


ani = animation.FuncAnimation(fig, updatefig, frames = range(100), interval = 100, blit = True)
plt.show()



