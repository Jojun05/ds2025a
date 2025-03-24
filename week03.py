def inters(l1, l2):
    l3 = []
    for v in l1:
        if v in l2:
            l3.append(v)
    return l3


l1 = [2, 32, 1, 44, 55, 66, 77]
l2 = [23, 2, 6, 32, 1, 55, 66, 13, 19, 29]
