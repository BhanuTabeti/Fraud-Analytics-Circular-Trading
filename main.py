import time
import numpy as np
from Src.utils import Read, GetNodeCnt, GenGraph
from Src.cluster import SpectralClustering, KMeans

if __name__ == "__main__" :
    # Read data
    data = Read("./Resources/dataset.csv", describe=True)

    # data = np.array([[1,2,1],[3,4,1]])

    start = time.time()
    # Generated graph from data
    W = GenGraph(data)
    end = time.time()
    print("%.10f" %(end-start))

    start = time.time()
    # Obtained eigenvalues and vectors of laplacian
    values, vectors = SpectralClustering(W, vectors=1)
    end = time.time()
    print("%.10f" %(end-start))

    start = time.time()
    # Applying KMeans on the embedded graph
    clusters = KMeans(vectors, k=2)
    end = time.time()
    print("%.10f" %(end-start))

    with open("./Resources/clusters.txt", "w") as f:
        f.write("%d\n" %len(W))
        for cluster in clusters :
            f.write("%d\n" %cluster)
