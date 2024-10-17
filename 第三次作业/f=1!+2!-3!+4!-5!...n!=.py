def factorial(n):
    sum,m = 1,1
    for i in range(2,n+1):
        m *= i
        sum += m*((-1)**i)
    return sum
n = int(input("请输入一个数:"))
print("f=1!+2!-3!+4!-5!...n! =",factorial(n))
