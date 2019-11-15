import numpy as np
from scipy.linalg import eigh
from .utils import GetNodeCnt, Compress
from sklearn.cluster import KMeans as kmeans

def KMeans(data, k=10) :
    # Performs clustering and returns the labels
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
    W = np.zeros((n, n), dtype="int")

    # Dictonary of neighbors
    d = {}
    for _ in range(n) :
        d[_] = []

    # Iterating data to populate incoming edges to a node
    for pt in data :
        d[int(pt[1])-1].append(int(pt[0])-1)

    # Optimization we came up with to exploit sparsity of the matrix
    sets = [set() for _ in range(n)]

    # For every pair of neighbors of the current vertex, add 1 to the corresponding entry
    for key, value in d.items() :
        for i in range(len(value)) :
            for j in range(i+1, len(value)) :
                W[value[i], value[j]] += 1
                W[value[j], value[i]] += 1

                # Remove from the previous set
                if W[value[i], value[j]] > 1 :
                    sets[W[value[i], value[j]]-1].remove((value[i], value[j]))
                    sets[W[value[i], value[j]]-1].remove((value[j], value[i]))

                # Add to the current set
                sets[W[value[i], value[j]]].add((value[i], value[j]))
                sets[W[value[i], value[j]]].add((value[j], value[i]))

    return W, n, sets
