import numpy as np
from numba import jit
from matplotlib import pyplot as plt
import math

@jit
def dist(x1, y1, x2, y2):
    # 두 점 사이의 거리를 구하는 함수
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

@jit
def potential(pos):
    # surf : 실험판의 각 좌표에 대응되는 전위를 저장하기 위한 numpy 배열
    surf = np.zeros((380, 240))
    for i in range(surf.shape[0]):
        for j in range(surf.shape[1]):
            for posit in pos:
                r = dist(i, j, posit[0], posit[1])
                if r == 0:
                    surf[i][j] = 0
                    break
                # surf[i][j] += posit[2] / r   # 거리에 반비례하는 경우
                # 거리의 자연로그에 비례하는 경우
                surf[i][j] += posit[2] * (- math.log(dist(i, j, posit[0], posit[1])))
    return surf


# (x 좌표, y좌표, 전극의 부호)
dipole = np.array([(90, 120, 1), (290, 120, -1)])  # dipole
round = [] # 원형 전극
y_line = [(90, i, 1) for i in range(70, 170, 1)] + [(290, i, -1) for i in range(70, 170, 1)] # 막대 전극 (y방향)
x_line = [(i, 120, 1) for i in range(40, 140, 1)] + [(i, 120, -1) for i in range(240, 340, 1)] # 막대 전극 (x방향)

# 원형 전극을 구성하는 점들을 저장
for i in range(380):
    for j in range(240):
        for posit in dipole:
            if 6.7 < dist(i, j, posit[0], posit[1]) < 7.3:
                round.append((i, j, posit[2]))

# 전위를 계산함
surface = potential(dipole)

# 등전위선을 그림
plt.figure(figsize=(19/2, 6))
plt.contour(surface.T, levels=50)
plt.xticks(list(range(0, 380+20, 20)))
plt.yticks(list(range(0, 240+20, 20)))
plt.show()
