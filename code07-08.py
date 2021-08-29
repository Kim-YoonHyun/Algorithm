## 함수
# def is_queue_full():
#     global SiZE, queue, front, rear
#     if rear >= SIZE-1:
#         return True
#     else:
#         return False

def is_queue_full():
    global SiZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False



def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        return
    rear += 1
    queue[rear] = data
def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print('큐가 비었음')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 코드
# queue = ['커피', '녹차', '꿀물', '환타', '게토']
# front = -1
# rear = 4

en_queue('화사')
print(queue)
en_queue('솔라')
print(queue)
en_queue('문별')
print(queue)
en_queue('철수')
print(queue)
en_queue('영희')
print(queue)
de_queue()
print(queue)
de_queue()
print(queue)
en_queue('바둑이')
print(queue)

