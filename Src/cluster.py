import numpy as np
from scipy.linalg import eigh
from sklearn.cluster import KMeans as kmeans

def KMeans(data, k=10) :
    clusters = kmeans(n_clusters=k, init="k-means++").fit(data)
    return clusters.labels_

def SpectralClustering(W, vectors=2) :
    # Diagonal Matrix
    D = np.diag(np.sum(W, axis=1))

    # Laplacian
    L = D-W

    # Eigenvalue, eigenvector pair
    return eigh(L, eigvals=(0, vectors-1))
