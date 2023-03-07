# 檔案讀取、寫入

# open(路徑, mode='開啟模式')

# 絕對路徑 /Users/user/python/basic/test.txt
# 相對路徑 test.txt 或是 ./test.txt

mode = 'w'  # 覆寫
mode = 'r'  # 讀取
mode = 'a'  # 在原先資料後寫入

file = open('test.txt', mode='r')  # 開啟檔案
print(file.read())  # 讀所有東西出來
print(file.readline())  # 讀一行
print(file.readlines())  # 讀全部並自動變成一個列表

# 也可以用for loop 直接一行一行讀
for line in file:
    print(line)

file.close()


# 覆寫 encoding='utf-8' 才能支援中文
# file = open('./test.txt', mode='w', encoding='utf-8')
# file.write('\n測試')
# file.close()


# 使用with來做到自動執行 close()

with open('./test.txt', mode='w', encoding='utf-8') as file:
    file.write('\n測試')
