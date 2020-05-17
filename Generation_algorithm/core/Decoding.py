#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np

#解码函数 (dot函数是 矩阵相乘)   返回 POP_size*2 矩阵，每一个行向量是个体的（x1，x2）
#input: x*33 矩阵           #output：x*2
def decoding(temp_pop,DNA_size):
    # 解码矩阵（2*33）未转置  将二进制（100*33）矩阵转换为十进制（100*2）矩阵
    decod_matrix = np.zeros((2, DNA_size), dtype=np.int)
    for n in range(16):
        decod_matrix[0][n] = 2 ** (15 - n)
        decod_matrix[1][n] = 0
    for n in range(16, 32):
        decod_matrix[0][n] = 0
        decod_matrix[1][n] = 2 ** (31 - n)

    temp = temp_pop.dot(np.transpose(decod_matrix))
    extend = np.array([1/(float(2**16-1)),1/(float(2**16-1))])
    temp1 = temp*extend       #100*2矩阵，100个个体每个个体的x1和x2占所取值的比例   0<= x <=1
    temp2 = temp1*np.array([4.096,4.096])        #100*2矩阵
    return temp2 - np.array([2.048,2.048])               #100*2 矩阵，每一个行向量表示一个个体的（x1，x2）值

if __name__ == '__main__':
    pass


