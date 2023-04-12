from physica import getCharge
from physics import thisisFunction
from matplotlib import pyplot as plt
import numpy as np


def get_charge_graph():
    fig = plt.figure()
    X = np.load("great.npy")
    ny, nx = X.shape
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    xv, yv = np.meshgrid(x,y)
    ax = fig.add_subplot(111, projection='3d')
    graph = ax.plot_surface(xv, yv, X)
    fig.show()
    fig.savefig('./holly!')
    plt.plot(X)
    plt.show()
    plt.savefig('./단층')

    # plt.figure(figsize=(25, 25, 25))
    # plt.plot(np.load("great.npy"))
    # plt.show()


def determine(L, V):
    c_ideal = L*L/d
    X = np.load("great.npy")
    Q = 0
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Q += X[i][j]
    print(Q)
    c_real = 12.562 * Q / V
    print(c_ideal, c_real)
    print(100*(c_real-c_ideal)/c_real)


L = 16
d = 16
sep = 512
V = 100
getCharge(L, d, V, sep)
# thisisFunction(L, d, sep)
get_charge_graph()
determine(L, V)

# L = 40
# d = 5
# V = 2
# 111.52920178442264
# 2.832e-09 6.204615346945939e-09