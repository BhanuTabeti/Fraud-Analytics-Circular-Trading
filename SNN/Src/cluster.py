import numpy as np
from scipy.linalg import eigh
from .utils import GetNodeCnt, Compress
from sklearn.cluster import KMeans as kmeans

def KMeans(data, k=10) :
    clusters = kmeans(n_clusters=k, init="k-means++").fit(data)
    return clusters.labels_

def SpectralClustering(W, vectors=2) :
    # Diagonal Matrix
    D = np.diag(np.sum(W, axis=1))

    # Laplacian
    D = D-W

    # Eigenvalue, eigenvector pair
    return eigh(D, eigvals=(0, vectors-1))

def SNN(data) :
    # Number of nodes in the graph
    n = GetNodeCnt(data)

    # Compressing the edge list
    data = Compress(data)

    # Empty neighbor matrix
    W = np.zeros((n, n))

    # Dictonary of neighbors
    d = {}
    for _ in range(n) :
        d[_] = []

    # Iterating data to populate neighbors
    for pt in data :
        d[int(pt[0])-1].append(int(pt[1])-1)

    # For every pair of neighbors of the current vertex, add 1 to the corresponding entry
    for key, value in d.items() :
        for i in range(len(value)) :
            for j in range(i+1, len(value)) :
                W[value[i], value[j]] += 1
                W[value[j], value[i]] += 1

    return W
