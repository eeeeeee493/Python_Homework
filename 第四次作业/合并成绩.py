scores = [("土木001","张三",75),("土木001","李四",40),("土木002","王五",68),("土木003","赵六",82)]
addition = eval(input())
for i in range(len(addition)):
    addition[i] = list(addition[i])
    addition[i][2] = round(addition[i][2])
    addition[i] = tuple(addition[i])
scores.extend(addition)
scores.sort(key=lambda x:x[2])
scores.sort()
print(scores)
#合并成绩 刚刚把期中考试成绩按照班级进行了排序整理，还未打印，如下： scores = [("土木001","张三",75),("土木001","李四",40),("土木002","王五",68),("土木003","赵六",82)]，马上就又来了一批补考成绩，不过这批成绩不是整数，也未按照班级排序，形如： [("土木002","陈七",59.5),("土木001","刘八",100)]，请编写程序读入这批补考数据进行处理，将成绩四舍五入为整数，并添加到 scores 中，使班级仍然有序，然后输出。 例如 输入： [("土木002","陈七",59.5),("土木001","刘八",100)] 输出： [('土木001', '刘八', 100), ('土木001', '张三', 75), ('土木001', '李四', 40), ('土木002', '王五', 68), ('土木002', '陈七', 60), ('土木003', '赵六', 82)]