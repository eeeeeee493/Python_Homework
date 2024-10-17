def pal(n):
    return str(n) == str(n)[::-1]
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input("请输入正整数:"))
print(f"{n}是回文素数") if pal(n) and prime(n) else print(f"{n}不是回文素数")
