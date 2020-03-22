# Write a program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes. 

import numpy as np
import matplotlib.pyplot as plt
x = np.arange (0.0, 4.0, 0.1)
f = x
g = x**2
h = x**3
plt.title("Week 8 task")
plt.xlabel ("x value")
plt.ylabel ("Function")
plt.plot (x, f, "g.", label="f(x) = x")
plt.plot (x, g, "b.", label="g(x) = x^2")
plt.plot (x, h, "r.", label="h(x) = x^3")
plt.legend()
plt.savefig("8-plotting.png")

# reference:
    # videos posted on learnonline for this course