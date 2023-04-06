#  学生信息列表
stuList  =  [
        {'学号':  '18001',  '姓名':  '王一',  '成绩':  89},
        {'学号':  '18002',  '姓名':  '丁一',  '成绩':  95},
        {'学号':  '18003',  '姓名':  '于一',  '成绩':  85}
]

#  定义函数，按成绩或学号排序后逐个输出学生信息
def  printStuInfo(stuList,  key):
        stuList.sort(key=lambda  x:x[key])    #  利用lambda函数作为sort函数的关键参数值
        for  stu  in  stuList:
                print(stu)

#  调用函数，按成绩排序后逐个输出学生信息
print("按成绩排序后："  )
printStuInfo(stuList,  '成绩')

#  调用函数，按学号排序后逐个输出学生信息
print(  "按学号排序后："  )
printStuInfo(stuList,  '学号')