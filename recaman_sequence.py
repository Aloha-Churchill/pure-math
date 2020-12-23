from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt


# how long does it take for certain numbers to get reached?
def hitNums(n,a):
    hit_numbers = np.empty(100000, dtype=int)
    for i in range(len(n)):
        diff = n[i] - a[i]
        if(a[i] > len(hit_numbers)):
            break
        else:
            hit_numbers[a[i]] = diff

    x_hit = np.arange(len(hit_numbers))

    x_hit_normalized = []
    hit_nums_normalized = []
    for i in range(len(hit_numbers)):
        if hit_numbers[i] < 10000 and hit_numbers[i] > -10000:
            x_hit_normalized.append(i)
            hit_nums_normalized.append(hit_numbers[i])

    plt.scatter(x_hit_normalized, hit_nums_normalized)
    plt.show()


def main():
    # make i array for iterations
    arr = genfromtxt('recaman - Sheet1.csv', delimiter = ' ', dtype = int)
    n = arr[:,0]
    a = arr[:,1]

    plt.scatter(n,a)
    plt.show()

    hitNums(n,a)


main()



