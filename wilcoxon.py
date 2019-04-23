import numpy as np
from scipy.stats import wilcoxon

data = np.loadtxt('fusion.txt')
print(wilcoxon(data[9], data[8]))
