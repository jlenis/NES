import matplotlib.pyplot as plt
import pandas as pd
import os


cwd = os.path.dirname(os.getcwd())
print(pd.read_csv('{}/outputs/lm_bench/batcat_cache.csv'.format(cwd)))
lat = pd.read_csv('{}/outputs/lm_bench/batcat_cache.csv'.format(cwd))
plt.plot(lat['size'], lat['latency'])
# plt.axis('scaled')
plt.xscale('log')
plt.ylabel('Nanoseconds (ns)')
plt.xlabel('Size (MB)')
plt.show()
