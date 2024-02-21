import random 

number = None
start = input('請決定範圍最小值')
end = input('請決定範圍最大值')
start = int(start)
end = int(end)  
r = random.randint(start,end)
count = 0
while r != number :
    count += 1
    number = input('請輸入數字')
    number = int(number)
    if number == r :
        print('恭喜你猜對了！您在第',count,'次時猜對')
        break
    elif number > r :
        print('比您猜的數字要更小喔！')
    elif number < r :
        print('比您猜的數字還要大喔！')
    print('這是您猜的第',count,'次！')