# builtin_functions_and_packages.py

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Built-in Functions

# 1. np.random.randint()
# Description: Generates random integers.
# Example:
# np.random.randint(2, size=N) in code snippet 1

# 2. np.concatenate()
# Description: Concatenates arrays along a specified axis.
# Example:
# np.concatenate([np.ones(100) if bit_value == 1 else np.zeros(100) for bit_value in x]) in code snippet 3

# 3. np.arange()
# Description: Returns evenly spaced values within a given interval.
# Example:
# np.arange(bp / 100, 100 * len(x) * (bp / 100) + bp / 100, bp / 100) in code snippets 1, 3, 4, and 5

# 4. np.cos()
# Description: Computes the cosine of each element of the input array.
# Example:
# np.cos(2 * np.pi * f * t2) in code snippets 1, 3, and 4

# 5. plt.plot()
# Description: Plots lines and/or markers to the Axes.
# Example:
# plt.plot(t1, bit, linewidth=2.5) in code snippets 1, 3, and 4

# Packages

# 1. numpy (np)
# Description: NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# Example:
# import numpy as np

# 2. matplotlib.pyplot (plt)
# Description: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits.
# Example:
# import matplotlib.pyplot as plt

# 3. math (part of Python Standard Library)
# Description: The math module provides mathematical functions and constants.
# Example:
# import math

# 4. random (part of Python Standard Library)
# Description: The random module provides functions for generating random numbers.
# Example:
# import random

# 5. datetime (part of Python Standard Library)
# Description: The datetime module supplies classes for manipulating dates and times.
# Example:
# import datetime

# 6. os (part of Python Standard Library)
# Description: The os module provides a portable way of using operating system-dependent functionality.
# Example:
# import os

# 7. sys (part of Python Standard Library)
# Description: The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
# Example:
# import sys
