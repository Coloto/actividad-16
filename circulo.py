import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv('Classificaci%C3%B3_del_s%C3%B2l.csv')
df = a[['TIPUSSOL']]

df.TIPUSSOL.value_counts().plot.pie()
plt.show()