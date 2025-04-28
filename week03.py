def inters(l1, l2): #중복 제거 
    s1 = set(l1)
    s2 = set(l2) #set이 중복을 제거하기 위한 자료형 변수임

    # return list(s1.intersection(s2))
    return list(s1 - s2) 
    #그러면 s1 - s2를 함으로써 중복된 값을 제거함 그러면 print결과에선 차집합한 결과가 나오는것임


l1 = [2, 32, 1, 44, 55, 66, 77] #리스트 l1
l2 = [23, 2, 6, 32, 1, 55, 66, 13, 19, 29] #리스트 l2
print(inters(l1, l2)) #s1 - s2 차집합 결과 출력
