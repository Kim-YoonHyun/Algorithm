## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 변수
memory = []
root = None
name_ary = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스']


## 메인코드
node = TreeNode()
node.data = name_ary[0]
root = node
memory.append(node)
for idx, name in enumerate(name_ary[1:]):
    node = TreeNode()
    node.data = name

    current = root

    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                print(f'{idx}:{current.data}왼쪽에 {name}입력')
                break
            print(f'{current.data}의 왼쪽에는 {current.left.data}(이)가 있습니다.')
            current = current.left
            
        else:
            if current.right == None:
                current.right = node
                print(f'{idx}:{current.data}오른쪽에 {name}입력')
                break
            print(f'{current.data}의 오른쪽에는 {current.right.data}(이)가 있습니다.')
            current = current.right
    memory.append(node)

print('이진 탐색 트리 구성 완료')
print(root.left.left.data, '\n')

find_data = '마마무'
current = root
while True:
    if current.data == find_data:
        print(find_data, '발견')
        break
    elif current.data > find_data:
        print(f'{find_data}는 {current.data} 보다 작습니다. 왼쪽으로 이동')
        if current.left == None:
            print(f'{current.data}의 왼쪽에는 더이상 데이터가 없습니다.')
            print(f'{find_data}는 없습니다.')
            break
        current = current.left
    else:
        print(f'{find_data}는 {current.data} 보다 큽니다. 오른쪽으로 이동')
        if current.right == None:
            print(f'{current.data}의 오른쪽에는 더이상 데이터가 없습니다.')
            print(f'{find_data}는 없습니다.')
            break
        current = current.right
