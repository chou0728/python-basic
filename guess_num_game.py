# 猜數字遊戲

result = 77
guess = None
limit = 3
count = 0
is_out_of_limit = False

while guess != result and not (is_out_of_limit):
    if count < limit:
        guess = int(input("輸入數字: "))
        count += 1
        if guess < result:
            print('提示: 大一點')
        elif guess > result:
            print('提示: 小一點')
    else:
        is_out_of_limit = True

if is_out_of_limit:
    print('超過三次囉')
else:
    print('恭喜答對')
