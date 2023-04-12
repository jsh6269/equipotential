from math import *
import numpy as np
from matplotlib import pyplot as plt
from numba import jit


def convert(qArr, L):
    B = np.empty((L, L))
    cnt = 0
    for i in range(L):
        for j in range(L):
            B[i][j] = qArr[cnt]
            cnt = cnt + 1
    return B

# L = 25
# d = 5
# Q = 10


@jit
def goThrough(dist, i, j, L, d, sep):
    step_size = d / sep
    affected_x, affected_y = int(i / L), i - int(i / L) * L
    affect_x, affect_y = int(j / L), j - int(j / L) * L
    dhori = (affect_x - affected_x)**2 + (affect_y - affected_y)**2
    for k in range(1, sep+1):
        dz1 = k * step_size
        dz2 = (sep + 1 - k) * step_size
        dist[i][j] += dz1 / (dhori + dz1 ** 2) ** 1.5 + dz2 / (dhori + dz2 ** 2) ** 1.5


def getCharge(L, d, V, sep):
    dist = np.empty((L*L, L*L))
    from tqdm import tqdm
    for i in tqdm(range(L*L)):
        for j in range(L*L):
            goThrough(dist, i, j, L, d, sep)

    step_size = d / sep
    B = np.linalg.inv(dist*step_size)
    # plt.pcolor(B)
    # plt.colorbar()
    # plt.show()

    var = np.full((L*L, 1), V)
    C = convert(np.dot(B, var), L)
    np.save('./great.npy', C)
    plt.pcolor(C, cmap="viridis_r")
    plt.savefig("hahaha.png")
    plt.colorbar()
    plt.show()

