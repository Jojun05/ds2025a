from collections import deque
d = deque([91,17,33])
d.append(-14)
d.append(100) #enqueue
d.append(99)
for _ in range(len(d)):
    print(d.popleft()) #dequeue
