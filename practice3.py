import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
from scipy.stats import kde
df = pd.read_excel("sample.xlsx", sheet_name=None)
data = []

print(df)
df_copy = df.copy()
data.append(df_copy)
density = kde.gaussian_kde(data)
x = np.linspace(10,50,100)
y = density(x)

plt.plot(x,y)
plt.title("Density plot of the data")
plt.show()