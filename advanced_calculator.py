# 進階點的計算機
number1 = float(input("請輸入第一個數: "))
operator = input("請輸入運算符: ")
number2 = float(input("請輸入第二個數: "))

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    print(number1/number2)
else:
    print('不支援')
