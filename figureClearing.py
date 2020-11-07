# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

ax.plot([1, 2, 3])
ax.grid(True)

fig.clear(True)

fig.suptitle('matplotlib.figure.Figure.clear() \
function Example\n\n', fontweight="bold")

plt.show()
