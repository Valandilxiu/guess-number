# 產生一個隨機整數 1~100
# 芿使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

start = int(input('請輸入範圍開始值'))
stop = int(input('請輸入範圍結束值'))

r = random.randint(start, stop)
count = 0

while True:
    x = int(input("請輸入一個數字，猜答案"))
    count = count + 1
    
    if r < x:
        print(x, '比答案大')
    elif r > x:
        print(x, '比答案小')
    else:
        print('終於答對了! 答案是', x)
        print('總共猜了', count, '次')
        break

    print('你已經猜了', count, '次')