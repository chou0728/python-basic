# 判斷

rainy = True

if rainy:
    print('下雨')
else:
    print('沒下雨')


score = 100

if score == 100:
    print('100')
elif score > 80:
    print('80')
else:
    print('other')

# 且
if score >= 80 and rainy:
    print('test')


# 或沒有
if score > 80 or not rainy:
    print('test2')
