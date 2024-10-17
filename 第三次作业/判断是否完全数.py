def isperfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum == n
n = int(input("请输入一个整数："))
print(f"{n}是完全数") if isperfect(n) else print(f"{n}不是完全数")
