from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#定义登录框账号密码的元素名列表
userfield = ['user','username','name','yonghu','zhanghao','email','account','USERNAME','USER']
passfield = ['password','pass','pwd','mima','passwd','PASSWORD']

# 初始化一个谷歌浏览器实例：browser
browser = webdriver.Chrome()
# browser = webdriver.Firefox() #火狐较慢

# 最大化浏览器
browser.maximize_window() 

# 通过get()方法，打开一个url站点
browser.get("http://127.0.0.1/dvwa/login.php") 

#等待页面加载
time.sleep(2)

#问题：如何迭代寻找定位元素
# print(browser.find_element_by_name(userfield[1]))
for user in userfield:
    # print(browser.find_element_by_name(user))
    if browser.find_element_by_name(user):
        print(browser.find_element_by_name(user))

# browser.find_element_by_name(userfield[1]).send_keys("admin") #输入账户密码
# browser.find_element_by_name("password").send_keys("password")
# browser.find_element_by_name('Login').click() #登录