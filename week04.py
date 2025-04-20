

class Node:
    def __init__(self, data, link=None):
        self.data = data #이게 노트에 저장된 데이터임
        self.link = link #이건 노드를 가르키는 링크

#링크스 리스트이게 연결 리스트를 관리를 함
class LinkedList:
    def __init__(self):
        self.head = None #일단 연결 리스트의 첫번째 노드인 head를 초기화해 none으로 설정
        

    def append(self, data):
        #연결 리스트가 비어있다? 그러면 새로운 노드를 head로 설정
        if not self.head: #
            self.head = Node(data) #새로운 node객체를 생성하여 head에 저장
            return #함수 종료
            
        current = self.head #시작점을 head로 설정을 하고
        while current.link: #while None이 아니면 반복
            current = current.link  # move current 다음 노드로 간다는 소리임
        current.link = Node(data) #새로운 node 객체를 생성해

    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return

        previous = None
        while current:
            if target == current.data:
                previous.link = current.link #여기서
                current.link = None
            previous = current
            current = current.link


    def search(self, target):
        current = self.head
        while current: #bug fix
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.link
        return  f"{target}은(는) 링크드 리스트 안에 존재하지 않습니다."


    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} -> "
            current = current.link
        return result + "END"

#append search remove <- 이거 배웠음


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
# print(ll.is_find(99))
# print(ll.is_find(10))
print(ll.search(99))
print(ll.search(-9))
ll.remove(-9)
ll.remove(77)
print(ll)
