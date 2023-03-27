# 账户信息
user_dict  =  {'admin':  '123456'}
# 锁定账户信息
lock_list  =  []
# 登录次数
count=0
# 最大登录次数
count_max=3
while  True:
        username  =  input('请输入用户名：')
        password  =  input('请输入密码：')
        if username in lock_list:
            print('账户已锁定！')
        else:
            if username in user_dict and user_dict[username] == password:
                print('登录成功！')
                # 成功进入，退出程序
                break
            else:
                count += 1
                print('用户名或密码错误！')
                if count >= count_max:
                    lock_list.append(username)
                    print('账户已锁定！')
        if  username  in  lock_list  or  count  >=  count_max:
            break