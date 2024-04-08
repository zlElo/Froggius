import time
from froggius import Froggius
import matplotlib.pyplot as plt
import numpy as np

# initialising vars
frogger = Froggius(print_out=True)
list_times = []

for i in range(60):
    start_time = time.time()
    frogger.debug('Example Debug Message')
    final_time = (time.time() - start_time) * 1000
    if final_time != 0:
        list_times.append(final_time)

# calculate average
average = sum(list_times) / len(list_times)
print(f'Average time: {average}ms')

# visualize the data as a line chart
plt.figure(figsize=(12, 6))
plt.plot(np.array(list_times), label='Execution Times (ms)')
plt.xlabel('Run')
plt.ylabel('Execution Time (ms)')
plt.title('Froggius Execution Times')
plt.legend()
plt.grid(True)
plt.show()