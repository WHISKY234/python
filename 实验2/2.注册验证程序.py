print("注册程序")
print("请用户输入注册用户名和密码")
print("用户名规则：以'_'开头，长度在3-30个字符之间")
print("密码规则：由下划线、数字、字母组成，不允许有其他符号，长度在8-16个字符之间")
a=input("用户名:")
b=input("密码：")
if len(a)<3 or len(a)>30:
    print("用户名长度不符合规范")
else:
    if a[0]!='_':
        print("用户名输入不包含‘_’")
    else:
        if len(b)<8 or len(b)>16:
            print("密码输入不符合长度规则")
        else:
            if not b.search("[A-Za-z_0-9]{8,16}$", b):
                print("密码输入不包含‘_’")
            else:print("程序注册成功")

