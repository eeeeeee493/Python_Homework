def encryption(n):
    n += 5
    return str(n)[-1]
num = input("请输入四位数字的明文:")
end = ""
for i in range(4):
    end += encryption(int(num[i]))
print(f"{num}的密文是{end}")
