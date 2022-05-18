import math
from timeit import timeit
from numba import jit

def hypot(a, b):
    return math.sqrt(a ** 2 + b ** 2)

@jit
def hypot_jit(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(timeit('hypot(5, 6)', globals=globals()))
print(timeit('hypot_jit(5, 6)', globals=globals()))
print(timeit('hypot_jit(5, 6)', globals=globals()))

