#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
    遗传算法
    max f(x1,x2) = 100*(x2-x1**2)**2 + (1-x1)**2
    -2.048 < x1 < 2.048
    -2.048 < x2 < 2.048
    间隔：10^-4

    该函数有两个局部极大点，分别是：
    f（2.048，-2.048） = 3897.7342
    f（-2.048，-2.048） = 3905.9262
    后者为全局最大点
'''

import numpy as np

from Decoding import decoding
from RouletteWheelSelection import RouletteWheelSelection
from Generate import generate

DNA_size = 32                   #编码 染色体长度为32(16+16)
POP_size = 100                  #种群数量
CROSS_rate = 0.6                #交叉概率
MUTATION_rate = 0.1             #变异概率
T = 1000                        #遗传代数

def f(x1,x2):                   #求解函数/适应度函数
    return 100*(x2-x1**2)**2 + (1-x1)**2
def fitness(x1,x2):
    return 100*(x2-x1**2)**2 + (1-x1)**2
#初试化种群
# pop矩阵：POP_size * DNA_size
pop = np.random.randint(2,size = (POP_size,DNA_size))
#循环每一代
for times in range(T):
    fitness_matrix = []            #保留 父代+子代 个体的fitness
    next_generation = []            #本次选出的100个后代
    temp_pop = pop.copy()           #存储父代+交叉变异子代的个体
    #轮盘赌选100个个体
    de = decoding(temp_pop.copy(),DNA_size)
    cross_pop = RouletteWheelSelection(pop.copy(),100,de)
    #交叉变异
    cross_pop = generate(cross_pop.copy(),DNA_size,MUTATION_rate,CROSS_rate)
    #将交叉变异个体和父代合并
    temp_pop = np.append(temp_pop, cross_pop, axis=0)
    #精英保留5个，放入next_generation
    fit_temp_pop = decoding(temp_pop.copy(),DNA_size)
    for number in range(len(temp_pop)): #output:(100+x)*1
        fitness_matrix.append(fitness(fit_temp_pop[number][0],fit_temp_pop[number][1]))
    judge = [0] * len(fitness_matrix)       #判断fitness_matrix相应位置个体是不是已经精英保留
    for number in range(5):             #选择排序
        least = 0
        for n in range(0,len(fitness_matrix)):
            if fitness_matrix[n]>fitness_matrix[least] and judge[n]==0:
                least = n
        judge[least] = 1
        next_generation.append(temp_pop[least])         #保留fitness最大的5个精英
    #轮盘赌，从（95+x）个个体中选择95个放入next_generation
    de = decoding(temp_pop.copy(),DNA_size)
    w = RouletteWheelSelection(temp_pop.copy(),95,de)
    for number in range(len(w)):                        #将选出的95个个体进入next_generation中
        next_generation.append(w[number])
    #将next_generation复制给pop以循环
    pop = np.array(next_generation)
print(pop[0])               #每一个pop[0]都是上一代中最优秀的个体（除了第一代）
my_temp = decoding(pop[0],DNA_size)
print(fitness(my_temp[0],my_temp[1]))












