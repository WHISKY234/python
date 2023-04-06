def getMaxMin(a, b, c):


    max_num = a
    min_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    return max_num, min_num

a=int (input(":"))
b=int (input(":"))
c=int (input(":"))

max_num, min_num = getMaxMin(a, b, c)
print("最大值为",{max_num},"最小值为",{min_num}  )


