# import module
import pandas as pd

# mengambil dataset untuk ditampilkan
df = pd.read_csv('Iris.csv')
df.head()

# menampilkan dataset secara keseluruhan
df

# menampilkan beberapa kolom dari dataset 
data = df.iloc[:,1:4]
data