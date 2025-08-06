import numpy as np

def read_list_list(which, empty_end = True):

    f = open(str(which) + ".txt", "r")
    data = f.read()
    data = data.split("\n\n")
    data = [x.split("\n") for x in data]
    if empty_end:
        del data[-1][-1]
    for x in range(len(data)): 
        for y in range(len(data[x])): 
            data[x][y] = int(data[x][y])
    return data



def read_4(which, empty_end = True):

    f = open(str(which) + ".txt", "r")
    data = f.read()
    data = data.split("\n")
    stack = []
    for x in data: 
        inter = x.split(",") 
        inter = [y.split("-") for y in inter]
        stack.append(inter)
    return np.array(stack).astype(int)