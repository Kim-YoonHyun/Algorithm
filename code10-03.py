# 함수
def add_number(num):
    if num <= 1:
        return 1
    return num + add_number(num - 1)


# 전역
NUM = 10

# 메인
print(add_number(5))