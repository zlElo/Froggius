import time
from froggius import Froggius
import matplotlib.pyplot as plt
from loguru import logger
import numpy as np
import structlog
from time import sleep

# FROGGIUS
froggius = Froggius(print_out=True)
list_times_froggius = []

for i in range(60):
    start_time = time.time()
    froggius.debug('Example Debug Message')
    final_time = (time.time() - start_time) * 1000
    if final_time != 0:
        list_times_froggius.append(final_time)

# calculate average
average_froggius = sum(list_times_froggius) / len(list_times_froggius)
print(f'Average time froggius: {average_froggius}ms')

sleep(1)

# LOGURU
list_times_loguru = []

for i in range(60):
    start_time = time.time()
    logger.debug('Example Debug Message')
    final_time = (time.time() - start_time) * 1000
    if final_time != 0:
        list_times_loguru.append(final_time)

# calculate average
average_loguru = sum(list_times_loguru) / len(list_times_loguru)
print(f'Average time loguru: {average_loguru}ms')

sleep(1)

# STRUCTLOG
list_times_structlog = []

for i in range(60):
    start_time = time.time()
    structlog_logger = structlog.get_logger()
    structlog_logger.debug('Example Debug Message')
    final_time = (time.time() - start_time) * 1000
    if final_time != 0:
        list_times_structlog.append(final_time)

# calculate average
average_structlog = sum(list_times_structlog) / len(list_times_structlog)
print(f'Average time structlog: {average_structlog}ms')

# visualize the data as a line chart
plt.figure(figsize=(12, 6))
plt.plot(np.array(list_times_froggius), label='Froggius Execution Times (ms)')
plt.plot(np.array(list_times_loguru), label='Loguru Execution Times (ms)')
plt.plot(np.array(list_times_structlog), label='Structlog Execution Times (ms)')
plt.ylabel('Execution Time (ms)')
plt.title('Logger Execution Times, python 3.12.1 on macOS sonoma 14.4.1')
plt.legend()
plt.grid(True)
plt.show()