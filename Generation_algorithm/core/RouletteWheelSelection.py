#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

def fitness(x1,x2):
    return 21.5 + x1*np.sin(4*np.pi*x1) + x2*np.sin(20*np.pi*x2)

def RouletteWheelSelection(temp_pop, out_nub,w):
    # 计算适应度  调用decoding(temp_pop)计算每个个体的（x1，x2）带入f计算每个个体的适应度->N*1矩阵
    sum = 0
    fitness_matrix = []  # type = list
    fitness_density = []  # 密度矩阵
    for n in range(len(w)):
        fitness_matrix.append(fitness(w[n][0], w[n][1]))
        sum = sum + fitness_matrix[n]

    # 计算个体的累计适应度->N*1
    fitness_density.append(fitness_matrix[0])  # **********************
    for n in range(1, len(w)):
        fitness_density.append(fitness_matrix[n] + fitness_density[n - 1])
    # 累计适应度归一化
    for n in range(len(w)):
        fitness_density[n] = float(fitness_density[n] / sum)
    # 此时 fitness_density[-1] = 1.0   len(fitness_density) = 100
    # 轮盘赌
    out_pop = []  # 存储返回的矩阵
    # 循环out_nub次，每次循环从temp_pop中选择一个放入out_pop

    while len(out_pop) < out_nub:
        temp = np.random.rand()
        for m in range(len(fitness_density)):
            if temp > fitness_density[m]:
                out_pop.append(temp_pop[m])
                break
    return np.array(out_pop)

if __name__ == '__main__':
    pass



