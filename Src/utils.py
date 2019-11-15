import numpy as np
import pandas as pd

def Read(path, describe=False, head=False) :
    # Self explanatory
    df = pd.read_csv(path)

    if describe is True :
        print(df.describe())

    if head is True :
        print(df[0:5])

    return df.to_numpy()

def GetNodeCnt(data) :
    # Adding vertices to a set from the set of edges
    vertices = set()
    for pt in data :
        vertices.add(pt[0])
        vertices.add(pt[1])

    # Returning the number of unique elements in the set
    return len(vertices)

def GenGraph(data) :
    # Number of nodes
    n = GetNodeCnt(data)

    # generate matrix, undirected for clusters
    mtrx = np.zeros((n,n), dtype="float_")
    for pt in data :
        mtrx[int(pt[0]-1), int(pt[1]-1)] += pt[2]
        mtrx[int(pt[1]-1), int(pt[0]-1)] = mtrx[int(pt[0]-1), int(pt[1]-1)]

    return mtrx

def Compress(data) :
    s = set()

    # Removing repeated edges
    for pt in data :
        # Removing self edges and zero transactions
        if pt[0] != pt[1] and pt[2] != 0 :
            s.add((pt[0], pt[1]))

    return s
