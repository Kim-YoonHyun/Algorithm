## 함수 선언
def is_stack_full():
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    else:
        return False
def is_stack_empty():
    global SIZE, stack, top
    if top == - 1:
        return True
    else:
        return False
def push(data):
    global SIZE, stack, top
    if is_stack_full():
        return
    top += 1
    stack[top] = data
def pop():
    global SIZE, stack, top
    if is_stack_empty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


## 전역 변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드
push('꿀물')
push('녹차')
push('커피')
push('식혜')
push('소주')
push('맥주')
print(stack)

pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
print(stack)
pop()
pop()
print(stack)