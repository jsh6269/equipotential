from math import *
import numpy as np
from numba import jit
# def barch(rad, height, numlist):
#     disk = []
#     for i in range(1, rad+1):
#         for j in range(numlist[i]):
#             interval = 2*pi/j
#             for k in range(j):
#                 theta = interval * k
#                 disk.append((i*cos(theta), i*sin(theta), 0, 1))
#                 disk.append((i * cos(theta), i * sin(theta), height, -1))
#
# r = 25
# h = 40
# datalist = []
# for i in range(1, r+1):
#     for j in range(10):
#         datalist[i]=j

@jit
def getIt(x, y, z, a, L, d, sep):
    sum = 0.0
    step_size = d / sep
    for i in range(L):
        for j in range(L):
            q1 = a[i][j][0]
            q2 = a[i][j][sep+1]
            dx = abs(x-i)
            dy = abs(y-j)
            dz1 = z * step_size
            dz2 = (sep+1-z) * step_size
            this = q1 * dz1 / sqrt(dx**2+dy**2+dz1**2)**3 - q2 * dz2 / sqrt(dx**2+dy**2+dz2**2)**3
            sum += this
    return sum


# L = 25
# d = 5
# Q = 10.0
# minSt = 99999
# maxSt = 0
# what = []
# print("minSt: "+str(minSt))

# @jit
def thisisFunction(L, d, sep):
    cube = np.zeros((L, L, sep+2))
    step_size = d / sep
    # cube[:, :, 0] = torch.full((L, L), Q)
    # t = int(L/2)
    # temp = np.zeros((L, L))
    # # temp = np.random.rand(L, L)*14
    # temp[0:t, 0:t] = np.random.rand(t, t)*14
    # for i in range(t):
    #     for j in range(t):
    #         if i < j:
    #             temp[i][j] = temp[j][i]
    # for i in range(t, L):
    #     for j in range(0, t):
    #         temp[i][j] = temp[L-1-i][j]
    #     for j in range(t, L):
    #         temp[i][j] = temp[L-1-i][L-1-j]
    # for i in range(t):
    #     for j in range(t, L):
    #         temp[i][j] = temp[i][L-1-j]
    # temp = temp - np.mean(temp)
    # cube[:, :, 0] = cube[:, :, 0] + temp
    # cube[:, :, -1] = -cube[:, :, 0]

    X = np.load("great.npy")
    cube[:, :, 0] = X
    cube[:, :, -1] = -cube[:, :, 0]

    for i in range(L):
        for j in range(L):
            for k in range(1, sep+1):
                cube[i][j][k] = getIt(i, j, k, cube, L, d, sep)

    result = np.zeros((L, L))
    for i in range(L):
        for j in range(L):
            result[i][j] = sum(cube[i, j, 1:-1]) * step_size
    print(result)
    from matplotlib import pyplot as plt
    plt.pcolor(result)
    plt.colorbar()
    plt.show()
    return
#     st = sqrt(result.var())
#
#     if minSt > st:
#         minSt = st
#         np.save('./physica', cube[:, :, 0])
#         np.save('./result', result)
#     if maxSt < st:
#         np.save('./worst', cube[:, :, 0])
#     print(st)
#     return minSt, maxSt
#
#
# for epoch in range(50000):
#     minSt, maxSt = thisisFunction(minSt, maxSt)
# print(minSt)
