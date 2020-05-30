import random
from functools import cmp_to_key

datas = [[random.randrange(50),random.randrange(50)] for _ in range(5)]

def bubbleSort(datas:list):
    for i in range(len(datas)-1):
        for j in range(len(datas)-1):
            if datas[j] < datas[j+1]:
                datas[j],datas[j+1] = datas[j+1],datas[j]


def myCmp(data1, data2):
    cmp1 = data1[0] + data1[1] * 2
    cmp2 = data2[0] + data2[1] * 2

    if cmp1 > cmp2:
        return 1
    elif cmp1 < cmp2:
        return -1
    else:
        return 0

# [x, y]
# x + 2y
# [[27, 32], [22, 32], [1, 49], [20, 22], [28, 41]]

# [[91,27,32], [86,22,32], [99,1,49] .....]

print(datas)
datas.sort(key=cmp_to_key(myCmp))
print(datas)