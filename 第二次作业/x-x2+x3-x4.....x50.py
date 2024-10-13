x = eval(input("输入x为"))
Sum = 0
for i in range(1,51):
    Sum += x/i*((-1)**(i+1))
print("x-x/2+x/3-x/4.....x/50="+str(Sum))