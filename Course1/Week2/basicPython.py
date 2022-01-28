#  %%

from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# %%

### Create a 3x1 numpy array
a = np.array([1,2,3])

### Print object type
print(type(a))

### Print shape
print(a.shape)

### Print some values in a
print(a[0], a[1], a[2])

### Create a 2x2 numpy array
b = np.array([[1,2],[3,4]])

### Print shape
print(b.shape)

## Print some values in b
print(b[0,0], b[0,1], b[1,1])

### Create a 3x2 numpy array
c = np.array([[1,2],[3,4],[5,6]])

### Print shape
print(c.shape)

### Print some values in c
print(c[0,1], c[1,0], c[2,0], c[2,1])

### 2x3 zero array 
d = np.zeros((2,3))

print(d)

### 4x2 array of ones
e = np.ones((4,2))

print(e)

### 2x2 constant array
f = np.full((2,2), 9)

print(f)

### 3x3 random array
g = np.random.random((3,3))

print(g)

### Create 3x4 array
h = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])

print(h)

### Slice array to make a 2x2 sub-array
i = h[:2, 1:3]

print(i)

print(h[0,1])

### Modify the slice
i[0,0] = 1738

### Print to show how modifying the slice also changes the base object
print(h[0,1])

### Integer
j = np.array([1, 2])
print(j.dtype)  


### Float
k = np.array([1.0, 2.0])
print(k.dtype)         

### Force Data Type
l = np.array([1.0, 2.0], dtype=np.int64)
print(l.dtype)


# %%

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))


# %%

x = np.array([[1,2],[3,4]])

### Compute sum of all elements; prints "10"
print(np.sum(x))

### Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=0)) 

### Compute sum of each row; prints "[3 7]"
print(np.sum(x, axis=1))


# %%

x = np.array([[1,2],[3,4]])

### Compute mean of all elements; prints "2.5"
print(np.mean(x))

### Compute mean of each column; prints "[2 3]"
print(np.mean(x, axis=0)) 

### Compute mean of each row; prints "[1.5 3.5]"
print(np.mean(x, axis=1))


# %%

### Print Normal Random Variables
print(stats.norm.rvs(size = 10))


#%%

from pylab import *

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
plot(X,Y)
plot(X,CY,'r--')

show()

# %%

print(stats.norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6])))


# %%

print(np.random.seed())

# %%

print(np.random.seed())

# Generate 1000 Student’s T continuous random variables.
x = stats.t.rvs(10, size=1000)

sns.distplot(x, kde=False)


# %%

print(x.min(), x.max(), x.mean(), x.var(), sep="\n")
stats.describe(x)
# %%

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)

# %%

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.ylabel("amplitude")
plt.xlabel("time")
plt.title("Waves")
plt.legend(["sine","cosine"])


# %%

plt.subplot(2,1,1)

plt.plot(x, y_sin)
plt.title("Sine")

plt.subplot(2,1,2)

plt.plot(x, y_cos)
plt.title("Cosine")

# %%

url = "Cartwheeldata.csv"

df = pd.read_csv(url)



sns.lmplot(x='Wingspan', y='CWDistance', data=df)
plt.show()

sns.swarmplot(x='Gender', y='CWDistance', data=df)
plt.show()

sns.lmplot(x='Wingspan', y='CWDistance', data=df, fit_reg=False, hue="Gender")
plt.show()

# %%
