# 함수
def open_box():
    global COUNT
    print('상자 열기')
    COUNT -= 1
    if COUNT == 0:
        print('<<<선물 넣기>>>')
        return

    open_box()
    print('상자 닫기')


# 전역 변수
COUNT = 3


# 메인
open_box()