import random

datas = [i for i in range(50)]


def linearSearch(datas: list, num: int):
    for i in range(len(datas)):
        data = datas[i]

        if data == num:
            print("資料存在")
            return True

    return False


def binarySearch(datas: list, num: int):
    low = 0
    up = len(datas) - 1

    while low <= up:
        mid = (low + up) // 2
        midValue = datas[mid]

        print(low, mid,up, midValue)

        if midValue < num:
            low = mid + 1

        elif midValue > num:
            up = mid - 1
        else:
            return True

print(binarySearch(datas, 8))