def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)

    # return list(s1.intersection(s2))
    return list(s1 - s2)


l1 = [2, 32, 1, 44, 55, 66, 77]
l2 = [23, 2, 6, 32, 1, 55, 66, 13, 19, 29]
print(inters(l1, l2))
