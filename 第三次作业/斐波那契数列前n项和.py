def sumfib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a,b = 1,1
        sum = a+b
        for i in range(3,n+1):
            c = a + b
            sum += c
            a,b = b,c
        return sum
n = int(input("请输入斐波那契数列项数:"))
print(f"斐波那契数列前{n}项和为{sumfib(n)}")
