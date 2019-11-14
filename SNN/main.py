import time
import numpy as np
from Src.utils import Read, GetNodeCnt, GenGraph
from Src.cluster import SpectralClustering, KMeans, SNN

if __name__ == "__main__" :
    # Read data
    data = Read("./Resources/dataset.csv", describe=True)

    data = np.array([[1,2,1],[3,1,100], [3,4,1], [2,4,1], [1,4,100], [2,3,100], [2,3,10],[1,5,0],[2,5,0],[3,5,0],[4,5,0]])
    # Shared neighbor matrix
    W = SNN(data)

    # Writing to file for debugging
    with open("./Resources/clusters.txt", "w") as f:
        f.write("%d\n" %len(W))
        for i in range(len(W)) :
            for j in range(len(W)) :
                f.write("%d " %W[i][j])
            f.write("\n")
