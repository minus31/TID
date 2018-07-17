###  Library Issues (1 / 15)

plt.imshow() 는 받는 데이터를 0과 1사이로 scaling 한다. Automatically


### np.nan == np.nan -> False
Warning One has to be mindful that in Python (and NumPy), the nan's don’t compare equal, but None's do. Note that pandas/NumPy uses the fact that np.nan != np.nan, and treats None like np.nan.
In [11]: None == None
Out[11]: True

In [12]: np.nan == np.nan
Out[12]: False
So as compared to above, a scalar equality comparison versus a None/np.nan doesn’t provide useful information.

In [13]: df2['one'] == np.nan
Out[13]: 
a    False
b    False
c    False
d    False
e    False
f    False
g    False
h    False
Name: one, dtype: bool