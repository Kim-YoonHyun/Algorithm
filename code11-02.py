import random
## 함수 선언부
def find_min_index(ary):
    min_index = 0
    for i in range(1, len(ary)):
        if ary[min_index] > ary[i]:
            min_index = i
    return min_index

## 전역 변수부
before = [random.randint(33, 190) for _i in range(20)]
after = []


## 메인 코드부
print('정렬 전 -->', before)

for i in range(len(before)):
    min_pos = find_min_index(before)
    after.append(before[min_pos])
    del before[min_pos]
print('정렬 후 -->', after)