import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x in x_set:
        return x /21
    else:
        return 0

x_set = np.array([1,2,3,4,5,6])
X = [x_set,f]

prob = np.array([f(x_k) for x_k in x_set])

print(dict(zip(x_set,prob)))

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.bar(x_set,prob)
ax.set_xlabel("とりうる値")
ax.set_ylabel("確率")

print("np.all=",end="")
print(np.all(prob >= 0))

print("np.sum=",end="")
print(np.sum(prob))

plt.show()