import time
# 함수
def count_down(count):
    if count == 0:
        print('발사')
    else:
        print(count)
        time.sleep(1)
        count_down(count-1)

# 전역
COUNT = 5

# 메인
count_down(COUNT)