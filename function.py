# 函式

# 縮排的部分就是函式內部
def hello(name):
    print('hello' + name)


hello('小白')


def sum(num1, num2):
    return num1 + num2


value = sum(1, 2)

print(value)


def fn_no_return():
    print('test')

# 預設會return None


result = fn_no_return()
print(result)
