ids = {"180001","180002","180003","180004","180005","180006","180007","180008","180009","180010"}
python = {"180001","180003","180004","180005","180007"}
cplusplus = {"180002","180003","180005","180008","180010"}
in_it = sorted(python | cplusplus)
print(f'参加了程序设计课程学习的同学有{in_it}')
not_in_it = sorted(ids - python - cplusplus)
print(f'没有参加程序设课程学习的同学有{not_in_it}')
in_it_all = sorted(python & cplusplus)
print(f'同时参加了两门序设计课程的同学有{in_it_all}')
python = sorted(python)
print(f'只参加了 Python 程序设计课程学习的同学有{python}')
