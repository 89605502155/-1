import numpy as np
import pandas as pd
import tensorly as tl
import os
dataset =pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/X — копия/01.txt', sep= ' \t')
dataset =  dataset.fillna( 0)
fds = sorted(os.listdir('C:/Users/admin/Desktop/курсовая 2.0/X — копия/')) #формируем список файлов для считывания в цикле
print(fds)
k = 0

while k < 35:
    dataset = pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/X — копия/'+fds[k],sep='\t')
    dataset = dataset.fillna(0)
    k = k + 1
    print(dataset)
    print()
    print(k)
    print()
