student1 = {'id': '21003130602', 'name': '张三'}
student2 = {'id': '21003130604', 'name': '李四'}
student3 = {'id': '21003130603', 'name': '王五'}
student4 = {'id': '21003130601', 'name': '赵六'}

list = [student1, student2, student3, student4]

list = sorted(list, key=lambda k: k['id'])

for student in list:
    print(student['id'], student['name'])