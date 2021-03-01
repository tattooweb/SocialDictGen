import urllib.request
import json

url = "http://127.0.0.1/dvwa/login.php"

headers={'Host':'127.0.0.1',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
         'Connection':'keep-alive',
         'Upgrade-Insecure-Requests':'1',
         'Referer':'http://127.0.0.1/dvwa/login.php'}
request = urllib.request.Request(url, data=None, headers=headers)
response = urllib.request.urlopen(request).read()
response = json.loads(response)
test = response["test"] 
print (test)
# req = request.form.get('xxx')