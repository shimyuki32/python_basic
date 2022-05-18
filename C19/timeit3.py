import time
from timeit import timeit

def snooze():
    time.sleep(1)

seconds = timeit('snooze()', globals=globals(), number=1)
print(f"{seconds:.4f}")