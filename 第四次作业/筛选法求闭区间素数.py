first,last = eval(input())
ls = list(range(first,last+1))
lsd = []
for i in ls:
    for j in range(2,i):
        if i%j==0:
            lsd.append(i)
            break
lse =[x for x in ls if x not in lsd]
print(lse)
#筛选法求素数 输入范围 first 和 last ，假设 first<last 并且二者均 >2 ，编写程序使用筛选法以列表形式输出该区间内所有的素数 例如 输入： 100,200 输出：[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]