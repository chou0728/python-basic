# for 迴圈

# for letter in "hello":
#     print(letter)

# 以下三種方式都相等
for num in [0, 1, 2, 3]:
    print(num)

for num in range(0, 4):
    print(num)

for num in range(4):
    print(num)


def custom_pow(base, pow):
    result = 1
    for num in range(pow):
        result = result * base
    return result


print(custom_pow(2, 3))
