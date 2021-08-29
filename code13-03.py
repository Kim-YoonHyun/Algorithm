## 함수
def binary_search(ary, fdata):
    pos = -1
    start = 0
    end = len(ary) - 1
    while start <= end:
        mid = (start+end) // 2
        if fdata == ary[mid]:
            return mid
        elif fdata > ary[mid]:
            start = mid+1
        else:
            end = mid-1
    return pos


## 전역
data_ary = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
find_data = 162


## 메인
print('배열 --> ', data_ary)
position = binary_search(data_ary, find_data)
if position == -1:
    print('발견하지 못하였습니다.')
else:
    print(f'{find_data}는 {position} 위치에 있습니다.')