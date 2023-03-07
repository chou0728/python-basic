# 二維列表 巢狀迴圈

list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(list[0][1])


for row in list:
    for col in row:
        print(col)
