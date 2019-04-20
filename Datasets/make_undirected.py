import networkx as nx
import scipy.io as sio
import scipy.sparse as sps
from os import path

# datasets = ['cora', 'citeseer', 'pubmed', 'cora_multi', 'mlgene'
#             'amazon', 'facebook', 'movielens', 'blogcatalog', 'ppigs_trans', 'ppigs', 'reddit_trans']

# datasets = ['movielens', 'blogcatalog', 'ppigs_trans', 'reddit_trans']
datasets = ['amazon']

for dataset in datasets:
    print('working on dataset: ', dataset)
    file_name = path.join(dataset, 'adjmat.mat')
    new_name = path.join(dataset, 'adjmat_old.mat')
    adjmat = sio.loadmat(file_name)
    sio.savemat(new_name, adjmat)

    adj = adjmat['adjmat']
    graph = nx.from_scipy_sparse_matrix(adj)
    adj = nx.adjacency_matrix(graph)

    if not isinstance(adj, sps.csr_matrix):
        adj = sps.csr_matrix(adj)

    adjmat['adjmat'] = adj
    sio.savemat(file_name, adjmat)

