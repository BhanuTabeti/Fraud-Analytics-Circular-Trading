import numpy as np
from scipy.linalg import eigh

def KMeans(data, k=10, iters=5) :
    # Random assignment
    centers = np.random.rand(k,data.shape[1])
    clusters = np.random.randint(k, size=len(data), dtype="int_")

    for _ in range(iters) :
        # Assigning clusters
        tmp = np.zeros(len(data), dtype="int_")
        minDist = np.ones(len(data), dtype="float_")*1e30
        for (idx, pt) in zip(range(len(data)), data) :
            for (cluster, center) in zip(range(len(centers)), centers) :
                curDist = np.linalg.norm(pt-center)
                if curDist < minDist[idx] :
                    minDist[idx] = curDist
                    tmp[idx] = cluster


        # Recomputing centers
        count = np.ones(k)
        for (pt, idx) in zip(data, tmp) :
            count[idx] += 1
            centers[idx] += pt

        for _ in range(k) :
            centers[_] /= count[_]


        # Convergence condition
        if np.array_equal(tmp, clusters) :
            break

        clusters = tmp

    return clusters

def SpectralClustering(W, k=2) :
    # Diagonal Matrix
    D = np.diag(np.sum(W, axis=1))

    # Laplacian
    L = D-W

    # Eigenvalue, eigenvector pair
    return eigh(L, eigvals=(0, k-1))
