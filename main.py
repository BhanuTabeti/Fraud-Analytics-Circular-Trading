import time
import numpy as np
from Src.utils import Read
from Src.cluster import SpectralClustering, KMeans

if __name__ == "__main__" :
    # data = Read("./Resources/dataset.csv", describe=True)
    # data = np.random.rand(2500, 2500)
    # values, vectors = SpectralClustering(data, 1)
    # clusters = KMeans(vectors, k=2)

    begin = time.time()
    for _ in range(30000) :
        foo = np.random.rand(1000, 1000)
        bar = foo*foo
    end = time.time()

    print("%.10f" %(end-begin))
