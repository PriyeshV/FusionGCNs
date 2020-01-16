import numpy as np
from scipy.stats import wilcoxon

data = np.loadtxt('fgcn-aistats.txt')
print(wilcoxon(data[3], data[0]))
