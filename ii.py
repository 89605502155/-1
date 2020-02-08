import numpy as np
import pandas as pd
import tensorly as tl
dataset =pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/X — копия/01.txt',sep='\t')
dataset = dataset.fillna(0)
print(dataset)
