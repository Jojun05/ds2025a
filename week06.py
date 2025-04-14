class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node #move

    def dequeue(self):
        if self.front is None:
            raise  IndexError("Queue is empty")
        self.size = self.size - 1

        temp = self.front
        self.front = self.front.link #move 프론트증가
        temp.link = None
        if self.front is None:
            self.rear = None
        return temp.data

q = Queue()
q.enqueue("Data stucture") #<-이게 프론트
q.enqueue("DataBase") #<- 이건 데이터베이스
print(q.size,q.front.data,q.rear.data)
print(q.dequeue())
print(q.size,q.front.data,q.rear.data)
print(q.dequeue())
print(q.size,q.front,q.rear)
