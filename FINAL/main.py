import time
import numpy as np
import pandas as pd
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

def ClusterGraph(clusters) :
    # Used in generating mapping
    index = np.zeros(n, dtype="int")

    # Keeps track of which nodes are in a cluster
    dictCluster = {}
    for _ in range(n) :
        dictCluster[_] = []

    # Holds mapping in a cluster
    dictMap = {}
    for (node, cluster) in zip(range(n), clusters) :
        dictMap[node] = index[cluster]
        dictCluster[cluster].append(node)
        index[cluster] += 1

    # Holds matrix for a cluster
    dictMatrix = {}
    for (cluster, clusterSize) in zip(range(n), index) :
        dictMatrix[cluster] = np.zeros((clusterSize, clusterSize), dtype="float_")

    # Populating the matrix
    for pt in data :
        if pt[0] != pt[1] and pt[2] != 0 and clusters[int(pt[0])] == clusters[int(pt[1])] :
            dictMatrix[clusters[int(pt[0])]][dictMap[int(pt[0])]][dictMap[int(pt[1])]] += 1

    return dictMatrix, dictMap, dictCluster

def FindCycles(graph, maxLen = 2) :
    # To not overwrite graph
    tmp = graph

    # Optimizing cycle length
    maxLen = min(maxLen, len(graph))

    # Keeps track frauds relative to the current indexing
    fraud = []

    # Generating _ length paths
    for _ in range(maxLen+1) :
        # Cheking if a cycle of length _ exists 
        for i in range(len(graph)) :
            if tmp[i][i] != 0 :
                fraud.append(i)

        # Generating next length paths
        tmp = tmp@graph

    return tmp, fraud


if __name__ == "__main__" :
    # Dummy dataset
    # data = np.array([[0,1,100], [1,2,200], [1,3,100], [2,0,1], [3,2,4], [3,1,50]])
    
    # Read the dataset
    data = Read("./Resources/dataset.csv", describe=True)

    # Timing SNN implementation
    start = time.time()
    W, n, sets = SNN(data)
    end = time.time()


    print("SNN took %.10f seconds." %(end-start))

        
    # Initialzing cluster representatives and sizes
    leaders = np.array((range(n)))
    sizes = np.ones(n)

    # We found that this threshold is good after some analysis
    thresh = 6

    # Timing the clustering process based on the current threshold
    start = time.time()
    for i in range(thresh, n) :
        for j in sets[i] :
            Merge(j[0], j[1])
    end = time.time()

    print("Clustering took %.10f seconds." %(end-start))

    # The clusters generated
    final = np.array([GetLeader(_) for _ in range(n)], dtype="int")

    # Graphs corresponding to clusters
    graphs, indices, clusters = ClusterGraph(final)

    # print(clusters)

    fraud = set()
    for cluster, graph in graphs.items() :
        # If cluster is not empty
        if len(graph) != 0 :
            _, fraudNodes = FindCycles(graph)

            # If node from the cluster has it's mapped index in the fraud nodes
            for node in clusters[cluster] :
                if indices[node] in fraudNodes :
                    fraud.add(node)

    print(len(fraud))