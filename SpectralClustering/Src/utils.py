import pandas as pd

def Read(path, describe=False, head=False) :
    df = pd.read_csv(path)

    if describe is True :
        print(df.describe())

    if head is True :
        print(df[0:5])

    return df.to_numpy()
