import numpy as np
from Src.utils import Read, GetNodeCnt, GenGraph
from Src.cluster import SpectralClustering, KMeans, SNN

leaders, sizes = None, None

def GetLeader(a) :
    while a != leaders[a] :
        a = leaders[a]

    return a

def Merge(a, b) :
    lA, lB = GetLeader(a), GetLeader(b)

    if lA != lB :
        if sizes[lA] >= sizes[lB] :
            sizes[lA] += sizes[lB]
            leaders[lB] = lA
        else :
            sizes[lB] += sizes[lA]
            leaders[lA] = lB

if __name__ == "__main__" :
    data = np.array([[1,2,100], [1,3,200], [1,4,100], [2,3,1], [2,4,2], [3,4,5]])
    W, n = SNN(data)
    print(W)


    for thresh in range(n) :
        leaders = np.array((range(n)))
        sizes = np.ones(n)

        for i in range(n) :
            for j in range(i+1, n) :
                if W[i][j] >= thresh :
                    Merge(i, j)

        with open("./Resources/SNN_"+str(thresh)+".txt", "w") as f :
            for x in leaders :
                f.write("%d "%x)

        print("#"*100)
        print(thresh)
        print(leaders)
