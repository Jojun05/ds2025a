class Node:
    def __init__(self, data,link=None):
        self.data = data
        self.link = link
# = Node("ABC")
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data): #li 1을 가져가고 링크드리스트에 들어가서 리턴
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

