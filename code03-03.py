katok = ['다현', '정연', '솔라', '쯔위', '사나', '지효', '문별']

# print(katok)
def delete_data(position):
    klen = len(katok)
    katok[position] = None

    for i in range(position+1, klen, 1):
        katok[i-1] = katok[i]
        katok[i] = None

    del katok[klen-1]

delete_data(1)
print(katok)

delete_data(3)
print(katok)