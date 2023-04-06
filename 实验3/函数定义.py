def getMean(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


n = int(input("请输入n：  "))
nums = []                                       
for i in range(n):
    num = int(input("请输入第 % d个数： % (i + 1)"))
    nums.append(num)
mean = getMean(nums)
print("这 % d个数的平均值为： % f % ",n, mean)