## 함수 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')

def insert_node(find_data, insert_data):
    """
    node를 중간에 삽입하는 함수
    :param find_data: insert_data를 이 데이터 앞에 삽입
    :param insert_data: find_data 앞에 삽입할 새로운 데이터
    :return: 
    """
    global memory, head, current, pre   # 전역변수 설정

    if head.data == find_data:  # 첫 노드 앞에 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()   # 마지막 노드에 삽입
    node.data = insert_data
    node.link = node
    return

def delete_node(delete_data):
    global memory, head, current, pre
    if head.data == delete_data:
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del (current)
            return
            pass

def find_data(find_data):
    global memory, head, current, pre
    current = head
    if head.data == find_data:
        return head
    while (current.link != None):
        current = current.link
        if current.data == find_data:
            return current
    return Node()

## 전역 변수부
memory = []     # 노드를 저장할 공간
head, current, pre = None, None, None
data_array = ['다현', '정연', '솔라', '쯔위', '사나', '지효', '문별']


## 메인 코드부
node = Node()   # 첫 번째 노드
node.data = data_array[0]
head = node
memory.append(node)
for data in data_array[1:]:
    # 이전 노드 임시보관
    pre = node

    # 다음 노드 설정
    node = Node()
    node.data = data

    # 이전 노드 link 에 다음 node 설정
    pre.link = node
    memory.append(node)


insert_node('쯔위', '화사')
print_nodes(head)
print()
delete_node('지효')
print_nodes(head)
print()
a = find_data('솔라')
print(a)