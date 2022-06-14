Import module pandas untuk yang akan digunakan untuk menampilkan dataset
```
import pandas as pd
```
Menampilkan beberapa dataset dengan menggunakan perintah: 

```
df = pd.read_csv('Iris.csv')
df.head()
```
Output: 
```
	Id	SepalLengthCm	SepalWidthCm	PetalLengthCm   PetalWidthCm	Species
0	1	5.1	            3.5	            1.4	            0.2	            Iris-setosa
1	2	4.9	            3.0	            1.4	            0.2	            Iris-setosa
2	3	4.7	            3.2	            1.3	            0.2	            Iris-setosa
3	4	4.6	            3.1	            1.5	            0.2	            Iris-setosa
4	5	5.0	            3.6	            1.4	            0.2	            Iris-setosa

```
Untuk menampilkan dataset secara keseluruhan menggunakan perintah: 
```
df
```
Output: 
```
	Id	SepalLengthCm	SepalWidthCm	PetalLengthCm PetalWidthCm	Species
0	1	5.1	            3.5	            1.4	          0.2	        Iris-setosa
1	2	4.9	            3.0	            1.4	          0.2	        Iris-setosa
2	3	4.7	            3.2	            1.3	          0.2	        Iris-setosa
3	4	4.6	            3.1	            1.5     	  0.2	        Iris-setosa
4	5	5.0	            3.6	            1.4 	      0.2	        Iris-setosa
...	...	...	            ...	            ...	          ...	        ...
145	146	6.7	            3.0	            5.2	          2.3	        Iris-virginica
146	147	6.3	            2.5	            5.0	          1.9	        Iris-virginica
147	148	6.5	            3.0	            5.2	          2.0	        Iris-virginica
148	149	6.2	            3.4	            5.4	          2.3	        Iris-virginica
149	150	5.9	            3.0	            5.1	          1.8	        Iris-virginica

150 rows × 6 columns
```

Menampilkan dataset dari kolom 1 sampai 3

```
data = df.iloc[:,1:4]
data
```

Output: 
```
	Id	SepalLengthCm	SepalWidthCm	PetalLengthCm 	
0	1	5.1	            3.5	            1.4	          	        
1	2	4.9	            3.0	            1.4	          	        
2	3	4.7	            3.2	            1.3	          	        
3	4	4.6	            3.1	            1.5     	  	        
4	5	5.0	            3.6	            1.4 	      	        
...	...	...	            ...	            ...	          	        
145	146	6.7	            3.0	            5.2	          	        
146	147	6.3	            2.5	            5.0	          	        
147	148	6.5	            3.0	            5.2	          	        
148	149	6.2	            3.4	            5.4	          	        
149	150	5.9	            3.0	            5.1	          	        

150 rows × 3 columns
```
