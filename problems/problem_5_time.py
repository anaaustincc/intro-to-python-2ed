"""
Print the elapsed time
"""

import time

start = time.time()
print(start)
input("Press enter to START the timer: ")
input("Press enter to STOP the timer: ")
end = time.time()
elapsed = end - start

print(f"Elapsed time: {elapsed} seconds")