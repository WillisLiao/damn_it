import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
import pandas as pd
import scipy.stats
list1=[]
df = pd.read_excel("sample.xlsx", sheet_name=None, usecols=["成績"])
#print(df)
list1.append(df)
print(list1)


#plt.hist(list1,bins=[10,20,30,40,50])
#plt.show()

