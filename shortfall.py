import numpy as np
from scipy.stats import rankdata


data = np.loadtxt('fgcn-aistats.txt').T
# data = np.loadtxt('skip-anal.txt').T
# data = np.loadtxt('fusion-models.txt').T

n_datasets, n_models = data.shape
print(n_datasets, n_models)
rank = np.zeros(data.shape)
print(data[1, :])
print(rankdata(1 - data[1, :], 'min'))

for i in range(n_datasets):
    rank[i, :] = rankdata(1 - data[i, :], 'min')
print(rank)
print('Rank: ', np.round(np.mean(rank, axis=0), 3))

score = np.zeros_like(rank)
shortfall = np.zeros_like(rank)
for i in range(n_datasets):
    score[i, :] = data[i, rank[i, :] == 1][0] - data[i, :]
    shortfall[i, :] = score[i, :]/max(score[i, :])
print('Penalty: ', np.round(np.mean(score, axis=0), 3))
print('Shortfall: ', np.round(np.mean(shortfall, axis=0), 3))


