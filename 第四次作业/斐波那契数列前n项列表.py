n = int(input())
if n == 1:
    print("1")
else:
    ls = [1,1]
    for i in range(2,n):
        ls.append(ls[i-2]+ls[i-1])
    print(ls)
#使用列表输出斐波那契数列的前 n 项，其中 n 由用户输入。 例如：输入 10 输出 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]