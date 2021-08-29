## 선택 정렬
def selection_sort(ary):
    n = len(data_ary)
    for pre_index in range(n - 1):
        max_index = pre_index
        for next_index in range(pre_index + 1, n):
            if data_ary[max_index] < data_ary[next_index]:
                max_index = next_index
        data_ary[pre_index], data_ary[max_index] = data_ary[max_index], data_ary[pre_index]


## -100 부터 100까지 숫자를 랜덤하게 30개 만들기
## 내림차순으로 정렬하기
import random
data_ary = [random.randint(-100, 100) for _ in range(30)]
print(data_ary)
selection_sort(data_ary)
print(data_ary)
