'''
author: malin
本人的第一个python小程序
因为我热爱音乐剧，在抢德奥gala的时候被黄牛逼疯了
所以自学python，写个抢票脚本，以后抢票都能用
会不定期维护
代码开源，有问题联系我
喜欢的点个star支持一下谢谢
qq:240814476
'''
from splinter.browser import Browser
from time import sleep
# traceback模块被用来跟踪异常返回信息
import traceback

# 设定用户名、密码
username = str(input("用户名:"))
passwd = str(input("密码:"))

print('黑牛抢票，你值得拥有')
print(username)
print(passwd)
