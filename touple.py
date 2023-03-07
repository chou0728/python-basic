# 元組
scores = (10, 20, 30, 40)

# 能用的方法都跟列表ㄧ樣，只差在一但定義後就不能做更動
# 要避免被修改的資料可以使用

scores[0] = 50

print(scores)
# TypeError: 'tuple' object does not support item assignment
