score = eval(input('第一次成绩:'))
score_new = eval(input('第二次成绩:'))
for name in score_new.keys():
    if name in score:
        if score[name] < score_new[name]:
            score[name] = score_new[name]
    else:
        score[name] = score_new[name]
print(score)
