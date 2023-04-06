#  创建文件并写入数据
with  open('seek.txt',  'w')  as  f:
        f.write('This  is  a  seek  test!')

#  定位并读取单词
with  open('seek.txt',  'r')  as  f:
        f.seek(10)    #  定位到    seek  test    的起始位置
        word  =  f.read(9)    #  读取    seek  test
        print(word)    #  输出    seek  test  