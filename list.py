# 列表
scores = [100, 90, 60]
max_list = [100, 'string', True]

print(scores[-1])  # 倒數第一位
print(scores[0:2])  # index 0 開始取不包含 index 2
print(scores[1:])  # index 1 開始取之後全部
print(scores[:2])  # index 2 開始取前面全部，不包含 index 2

# 字串也可以使用
phrase = 'hello my friend'
print(phrase[0: 3])


# 將列表延伸
scores.extend(max_list)
print(scores)

# 列表後再加上值
scores.append(1)
print(scores)

# 插入
scores.insert(2, 30)
print(scores)

# 刪除
scores.remove(30)
print(scores)

# 清掉最後一個
scores.pop()

# 清空
scores.clear()
print(scores)

# 排序
# scores.sort()

# 反轉
# scores.reverse()

# 出現次數
print(scores.count(100))
