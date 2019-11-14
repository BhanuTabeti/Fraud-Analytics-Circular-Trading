import time
import numpy as np
from Src.utils import Read, GetNodeCnt, GenGraph
from Src.cluster import SpectralClustering, KMeans

if __name__ == "__main__" :
    data = Read("./Resources/dataset.csv", describe=True)
    W = GenGraph(data)

    values, vectors = SpectralClustering(data, vectors=1)

    print(values)
    print(vectors)

    clusters = KMeans(vectors, k=2)

    print(clusters)
