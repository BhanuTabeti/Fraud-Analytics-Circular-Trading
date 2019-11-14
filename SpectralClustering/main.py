import time
import numpy as np
from Src.utils import Read
from Src.cluster import SpectralClustering, KMeans

if __name__ == "__main__" :
    data = Read("./Resources/dataset.csv", describe=True)
    eigenvalues, eigenvectors = SpectralClustering(data, 29)
    clusters = KMeans(vectors, k=30)
