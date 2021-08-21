## 함수 선언부
def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend


def insert_data(position, friend):  # 삽입 함수
    katok.append(None)
    klen = len(katok)
    for i in range(klen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None
    katok[position] = friend


def delete_data(position):
    klen = len(katok)
    katok[position] = None
    for i in range(position + 1, klen, 1):
        katok[i - 1] = katok[i]
        katok[i] = None
    del katok[klen - 1]


## 전연 변수부
katok = []
select = -1  # 1추가 2삽입 3삭제 4종료


## 메인 코드부
while select != 4:
    select = int(input('1추가 2삽입 3삭제 4종료--> '))

    if select == 1:
        friend = input('추가할 데이터--> ')
        add_data(friend)
    elif select == 2:
        position = int(input('삽입할 위치--> '))
        friend = input('추가할 데이터--> ')
        insert_data(position, friend)
    elif select == 3:
        position = int(input('삭제할 위치--> '))
        delete_data(position)
    elif select == 4:
        print(katok)
        break
    else:
        print('다시확인')
        continue
