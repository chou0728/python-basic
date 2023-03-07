# 類別class、物件object

# __init__ 建構函式第一個參數一定要傳入self，這個物件本身
class Phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == 'ios':
            return True
        else:
            return False


phone1 = Phone('ios', 123, True)
print(phone1.number)
phone2 = Phone('ios', 456, False)
print(phone2.number)
print(phone2.is_ios())
