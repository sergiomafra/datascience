## Comparison between a NumPy array anda pure Python list
## being multiplied by 2 ten time in a row

import numpy as np
import time


# Arrays
nparray = np.arange(1000000)
pparray = list(range(1000000))

# Numpy Time
start = time.time()
for _ in range(10):
    nparray = nparray * 2
stop = time.time()
nptime = stop - start
print(f'NumPy: {nptime}')

# Pure Python List
start = time.time()
for _ in range(10):
    pparray = [x*2 for x in pparray]
stop = time.time()
pptime = stop - start
print(f'Pure Python List: {pptime}')

# Comparison
print(f'NumPy was {pptime/nptime} times faster')

