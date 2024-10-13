PM = eval(input("请输入PM2.5值："))
if PM <0:
    print("这不是一个正确的值")
elif PM <= 50:
    print("空气质量为优")
elif PM <= 100:
    print("空气质量为良")
elif PM <= 150:
    print("空气质量为轻度污染")
elif PM <= 200:
    print("空气质量为中度污染")
elif PM <= 300:
    print("空气质量为重度污染")
else:
    print("空气质量为严重污染")
