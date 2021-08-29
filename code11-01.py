# 기본 정렬

def find_min_index(ary):
    min_index = 0
    for i in range(1, len(ary)):
        if ary[min_index] > ary[i]:
            min_index = i
    return min_index

test_ary = [55, 88, 33, 77]
min_pos = find_min_index(test_ary)
print(f'최솟값 --> {test_ary[min_pos]}')