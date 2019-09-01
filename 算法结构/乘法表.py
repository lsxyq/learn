#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s\t'%(j,i,j*i),end='')
#
#     print(end='\n')

# print('\n'.join(['\t'.join(['%s*%s=%s'%(j,i,j*i)for j in range(1,i+1)]) for i in range(1,10)]))


print('\n'.join(['\t'.join(['{}*{}={}'.format(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))



