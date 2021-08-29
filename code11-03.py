import random
## 함수
def selection_sort(ary):
    n = len(ary)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if ary[min_index] > ary[j]:
                min_index = j
        ary[i], ary[min_index] = ary[min_index], ary[i]
    return ary

## 전역
data_ary = [random.randint(33, 190) for _i in range(20)]

## 메인
print('정렬 전 -->', data_ary)
data_ary = selection_sort(data_ary)
print('정렬 gn -->', data_ary)