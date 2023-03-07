name = "eric"
age = 30

# using \n
print("hello\n" + name)

# using addition operator
print("I\"m " + name)

# using eparate everything with a comma
print("I\"m", name, "and age is", age)

# using .format() and {}
print("I\"m {} and age is {}".format(name, age))

# using f-strings
print(f"I\"m {name} and age is {age}")

# 字串method
print(name.upper())

# 串連並轉換型別
print(name.upper().isupper())

# 字串位置
print(name[1])
print(name.index('r'))

# 字串替換
print(name.replace('r', 'e'))

# 數字轉字串
print(f"I am {str(age)}")
