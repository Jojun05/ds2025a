from queue import Queue #queue 클래스를 가져와

q = Queue() #이건 비어있는 q임 

q.put("Data structure") #이걸 q에 추가 
q.put("Database") #이걸 q에 추가 2
q.put("Javascript") # 이걸 q에 추가 3
print(q.qsize()) #일단 q의 사이즈 3

print(q.get()) #q 중복 제거하고 반환을해 그럼 Data structure 이게 나옴 

print(q.qsize()) #다시 q의 사이즈 그럼 2
print(q.get()) #데이터를 다시 제거하고 반환 그럼 database
print(q.qsize()) #또 데이터 사이즈 1
print(q.get()) #이제 javascript
print(q.qsize()) #이럼 결과 0
