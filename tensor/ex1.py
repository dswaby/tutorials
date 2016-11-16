import numpy as np
import matplotlib.pyplot as plt

scores = np.array([1.0, 2.0, 3.0])


def softmax(x):
    print(np.sum(np.exp(x), axis=0))
    print(np.exp(x))
    return np.exp(x) / np.sum(np.exp(x), axis=0)


print(softmax(scores))

x = np.arange(-2, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
