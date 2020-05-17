#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

#对一个个体进行变异操作
def mutate(child,DNA_size,mutation_rate):
    for point in range(DNA_size):
        if np.random.rand() < mutation_rate:
            child[point] = 1-child[point]
    return child

#交叉变异 产生子代;两点交叉
#input： temp_pop : len(temp_pop)*DNA_size      output：？*33     ？为子代个数
def generate(temp_pop_gen,DNA_size,mutation_rate,CROSS_rate):
    out_pop = []
    cross_pop = []      #此时如果不初始化cross_pop，len（cross_pop） = 100
    cross_pop_rate = np.random.rand(len(temp_pop_gen))    #决定每个个体要不要交叉

    for cross_ind_index in range(len(temp_pop_gen)):         #在cross_pop中存储要交叉的个体
        if cross_pop_rate[cross_ind_index] < CROSS_rate:
            cross_pop.append(temp_pop_gen[cross_ind_index])

    #交叉 顺序找出cross_pop的两个进行交叉

    cross_nub = int(len(cross_pop)/2)                   #********
    #每两个的个体之间的交叉位置不同
    for n in range(cross_nub):
        cross_index = np.random.randint(1,33,size=2)    #两点交叉位置
        if cross_index[0]>cross_index[1]:
            cross_index = cross_index[::-1]             #asc 升序
        #交换位置 两点交叉产生的子代是偶数
        out_pop.append(cross_pop[2*n])
        out_pop.append(cross_pop[2*n+1])
        s = out_pop[2*n+1][cross_index[0]:cross_index[1]+1]
        out_pop[2*n+1][cross_index[0]:cross_index[1]+1] = out_pop[2*n][cross_index[0]:cross_index[1]+1]
        out_pop[2*n][cross_index[0]:cross_index[1]+1] = s

        #变异   此时子代是out_pop[2*n:2*n+2]
        out_pop[2*n] = mutate(out_pop[2*n],DNA_size,mutation_rate)
        out_pop[2*n+1] = mutate(out_pop[2*n+1],DNA_size,mutation_rate)
    return np.array(out_pop)

if __name__ == '__main__':
    pass



