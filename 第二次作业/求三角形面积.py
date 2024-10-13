a,b,c = eval(input("输入三角形三边，用英文逗号分开："))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print("该三角形面积为"+str(area))
else:
    print("不能构成三角形")
