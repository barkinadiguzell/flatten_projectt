l = [[1, 2, 3], [4, 5, 6], [7], [8, 9],[10],[11,12,13,14,15],[23,45],[54]]
def flatten(l):
    new_l = []
    
    for x in l:
        if hasattr(x,"__iter__"):
            new_l.extend(flatten(x))
        else:
            new_l.append(x)
    return new_l  