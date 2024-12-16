import numpy as np 

def load(line_splitter= "  ", to_int=False, to_list=False):

    with open('input.txt') as f:
        inp = f.read().splitlines()
        
        if to_list:
            inp = [list(x)for x in inp]
        if line_splitter:
            inp = [x.split(line_splitter) for x in inp]
        if to_int:
            inp = [[int(y) for y in x]for x in inp]
    return inp


def transform_13(data):
    processed_data = []
    stack = []
    for l in data:
        if "Button" in l:
            x,y = l.split(",")
            x = x.split("+")[1]
            y = y.split("+")[1]
            stack.append([x,y])
        elif "Prize" in l: 
            x,y = l.split(",")
            x = x.split("=")[1]
            y = y.split("=")[1]
            stack.append([x,y])    
            
        else:
            processed_data.append(stack)
            stack = []  
    return np.array(processed_data).astype(int)
