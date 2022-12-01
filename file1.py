import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm

df=pd.read_csv("Downloads/Cars93.csv")
#print(df)
df=df.head()
fig=plt.figure()
plt.title('Price range of all types of cars')
sns.boxplot(df.Price)
print("five number summary")
print(np.min(df.Price))
print(np.max(df.Price))
print(np.std(df.Price))
print(np.mean(df.Price))
print(np.median(df.Price))

#histogram
mode1=df['MPG.city'].mode()
print("\nhighest Frequency\n",mode1)
plt.hist(df['MPG.city'])
plt.title("frequency distribution")
plt.xlabel('MPG.city')
plt.show()

plt.scatter(df['Horsepower'],df['MPG.city'])
plt.title("Scatter plot")
plt.xlabel('Horsepower')
plt.ylabel('MPG.city')
plt.show()

plt.plot(df['EngineSize'])
plt.plot(df['Horsepower'])
plt.title("enginesize vs horsepower")
plt.xlabel('EngineSize')
plt.ylabel('Horsepower')
plt.show()

import pandas as pd
Series_A=pd.Series([10,20,30,40,50])
Series_B=pd.Series([40,50,60,70,80])
common=np.intersect1d(Series_A,Series_B)
print(common)

print(Series_A.sum())

print(se)
