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
    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            #print(current.data)
            result = result + str(current.data) + " -> "
            current = current.link
        return result + "END"
     #   return "Linked List"

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)
