import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Src.cluster import SNN
from Src.utils import Read, GetNodeCnt

# Used in clustering
leaders, sizes = None, None

def GetLeader(a) :
    # Continue while the current node is not the set representative
    while a != leaders[a] :
        a = leaders[a]

    return a

def Merge(a, b) :
    lA, lB = GetLeader(a), GetLeader(b)

    # Merge only if leaders are not same, that is, they don't belong to the same cluster
    if lA != lB :
        # Ensures log(N) complexity
        if sizes[lA] >= sizes[lB] :
            sizes[lA] += sizes[lB]
            leaders[lB] = lA
        else :
            sizes[lB] += sizes[lA]
            leaders[lA] = lB

if __name__ == "__main__" :
    # Dummy dataset
    # data = np.array([[1,2,100], [2,3,200], [2,4,100], [3,1,1], [4,3,4]])
    
    # Read the dataset
    data = Read("./Resources/dataset.csv", describe=True)

    # Timing SNN implementation
    start = time.time()
    W, n, sets = SNN(data)
    end = time.time()

    print("SNN took %.10f" %(end-start))

    table = []
    # Trying various thresholds
    for thresh in range(1, 20) :
        # Initialzing cluster representatives and sizes
        leaders = np.array((range(n)))

        sizes = np.ones(n)

        # Timing the clustering process based on the current threshold
        start = time.time()
        for i in range(thresh, n) :
            for j in sets[i] :
                Merge(j[0], j[1])
        end = time.time()

        print("Merge took %.10f" %(end-start))

        final = [GetLeader(_) for _ in range(n)]
        # with open("./Resources/SNN_"+str(thresh)+".txt", "w") as f :
        #     for x in final :
        #         f.write("%d "%x)
        
        # Obtaining counts for analysis
        unique, counts = np.unique(final, return_counts=True)
        table.append([thresh, (end-start), np.amax(counts), len(unique)])

        print("Threshold %d completed."%thresh)

    # Showing statistics
    df = pd.DataFrame(table, columns=["Threshold", "Time", "Maximal_cluster", "Total Clusters"])
    print(df)
    # ax = plt.gca()

    # df.plot(kind='line',x='Threshold',y='Total Clusters', color='green',ax=ax)
    # # df.plot(kind='line',x='Threshold',y='Maximal_cluster', color='red', ax=ax)
    # plt.title("Variation of Total Clusters with Threshold")
    # plt.ylabel("Total Clusters")

    # plt.show()