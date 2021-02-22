# encoding: utf-8
import sys,argparse
import pypinyin
import re

#TODO:改变输出字符颜色
ERROR_TIPS = "[ERROR**********]"
PROCESS = "[PROCESS++++++++++]"

'''
一阶密码：仅根据一项个人信息生成的密码

二阶密码：根据两项个人信息组合生成的密码,去除低于六位的密码

三阶密码：由于部分人喜欢在两项个人信息中间加入一个特殊符号，以加强密码复杂度和强度，
为了包含这种情况，故根据两项个人信息以及一个常用的连接符号（默认：.!_-#@:$&*~?%+=/|，
建议尽量减少连接符，否则会极大增加密码数量，甚至导致内存溢出从而生成失败）生成三阶密码


'''

#字符图
def str_pic():
	print(""" ____             _       _ ____  _      _    ____            
/ ___|  ___   ___(_) __ _| |  _ \(_) ___| |_ / ___| ___ _ __  
\___ \ / _ \ / __| |/ _` | | | | | |/ __| __| |  _ / _ \ '_ \ 
 ___) | (_) | (__| | (_| | | |_| | | (__| |_| |_| |  __/ | | |
|____/ \___/ \___|_|\__,_|_|____/|_|\___|\__|\____|\___|_| |_|

							------author by tattoo
""")
#命令行参数
# def parse_args():
#     parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u username [options...]")
#     #定义字典阶数
#     parser.add_argument("--level",type=int,choices=[1,2,3],help="[REQUIRED]the level of dict",required=True)
#     parser.add_argument("-u","--username",type=str)
#     parser.add_argument("-p","--password",type=str)
#     parser.add_argument("-cn","--cname",type=str)
#     parser.add_argument("-en","--ename",type=str)
#     parser.add_argument("-t","--tel",type=str)
#     parser.add_argument("-id","--idcard",type=str)
#     parser.add_argument("-b","--birthday",help='Example: 19990523 or 0523')
#     parser.add_argument("-m","--mail",type=str)
#     parser.add_argument("-q","--qq",type=str)
#     return parser.parse_args()
def parse_args():
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u username [options...]")

	#gendict
	gendict = parser.add_argument_group('GEN_DICT')
	#level定义生成字典的阶数，必选参数，默认为1，只能输入1,2,3
	gendict.add_argument("--level",type=int,choices=[1,2,3],help="[REQUIRED]the level of dict",default=1)
	gendict.add_argument("-u","--username",type=str)
	gendict.add_argument("-p","--password",type=str)
	gendict.add_argument("-cn","--cname",type=str)
	gendict.add_argument("-en","--ename",type=str)
	gendict.add_argument("-t","--tel",type=str)
	gendict.add_argument("-id","--idcard",type=str)
	gendict.add_argument("-b","--birthday",help='Example: 19990523 or 0523')
	gendict.add_argument("-m","--mail",type=str)
	gendict.add_argument("-q","--qq",type=str)


	#CAPTCHA_OCR-optical character recognition 
	CAPTCHA_OCR = parser.add_argument_group('CAPTCHA_OCR')
	CAPTCHA_OCR.add_argument('--ocr',action = "store")

	#BURST
	burst = parser.add_argument_group('BURST')
	burst.add_argument('--burst',action="store")

	parser.add_argument('--push', action='store')
	return parser.parse_args()
'''
	每个参数只能传一个值
    USERNAME = ["twodog"]
    PASSWORD = ["old_password"]
    CN_NAME = "李二狗"
    EN_NAME = "Bill"
    TEL = ["13512345678"]
    ID_CARD = "220281198309243953"
    BIRTHDAY = ("1983", "09", "24")
    EMAIL = ["987654321@qq.com"]
    QQ = ["987654321"]
'''

#class定义人像类
class Person():
	def __init__(self):
		self.username = ""
		self.password = ""
		self.cname = ""
		self.ename = ""
		self.tel = ""
		self.idcard = ""
		self.birthday = ""
		self.mail = ""
		self.qq = ""

#func获取拼音
def get_py(cname):
    result = ""
    for i in pypinyin.pinyin(cname, style=pypinyin.NORMAL):
        result += ''.join(i)
    return result

#func获取中文名字缩写
def get_abbreviation(cname):
	result = ""
	for i in cname:
		result += get_py(i)[0]
	return result

#func处理命令行参数,并转为列表类型
def get_args():
	args_list = []

	#处理参数-用户名
	username = []
	if args.username:
		username.append(args.username)
	else:
		username = ""

	#处理参数-密码
	password = []
	if args.password:
		password.append(args.password)
	else:
		password = ""

	#处理参数-中文名
	cname = []
	if args.cname:		
		cname_tmp = args.cname
		#form1-获取中文名字拼音
		cname_py = get_py(cname_tmp)
		#form2-获取拼音首字母
		cname_abbreviation = get_abbreviation(cname_tmp)
		#form3-首字母转成大写
		cname_abbreviation_upper = cname_abbreviation.upper()
		#传入cname列表中
		cname.append(cname_py)
		cname.append(cname_abbreviation)
		cname.append(cname_abbreviation_upper)
	else:
		cname = ""

	#处理参数-英文名
	ename = []
	if args.ename:
		ename_tmp = args.ename
		#form1-全小写
		ename_lower = ename_tmp.lower()
		#form2-首字母大写
		ename_init_upper = (ename_tmp[0].upper())+(ename_tmp[1:])
		#form3-全大写
		ename_upper = ename_tmp.upper()
		#传入ename列表中
		ename.append(ename_lower)
		ename.append(ename_init_upper)
		ename.append(ename_upper)
	else:
		ename = ""

	#处理参数-电话号码
	tel = []
	if args.tel:
		if len(args.tel) == 11:
			tel_tmp = args.tel
			#form1-号码后四位
			tel_last_four = tel_tmp[-4:]
			#form2-号码后六位
			tel_last_six = tel_tmp[-6:]
			#form3-全号码
			tel_full = tel_tmp
			#传入tel列表中
			tel.append(tel_last_four)
			tel.append(tel_last_six)
			tel.append(tel_full)
		else:
			print(ERROR_TIPS + "请输入11位电话号码！")
			sys.exit()
	else:
		tel = ""

	#处理参数-身份证号码
	idcard = []
	if args.idcard:
		idcard_tmp = args.idcard
		if args.idcard.isnumeric() and len(args.idcard) == 18:			
			#form1-id后四位
			idcard_last_four = idcard_tmp[-4:]
			#form2-id后六位
			idcard_last_six = idcard_tmp[-6:]
			#form3-id后八位
			idcard_last_eight = idcard_tmp[-8:]
			#传入idcard列表中
			idcard.append(idcard_last_four)
			idcard.append(idcard_last_six)
			idcard.append(idcard_last_eight)
		else:
			print(ERROR_TIPS + "请输入18位身份证号！")
			sys.exit()
	else:
		idcard = ""

	#处理参数-生日期
	birthday = []
	if args.birthday:
		birthday_tmp = args.birthday
		#有年份19990523
		if len(args.birthday) == 8:
			#form1-生日
			birthday_full = birthday_tmp
			#form2-生日后六位
			birthday_last_six = birthday_tmp[-6:]
			#form3-生日后四位
			birthday_last_four = birthday_tmp[-4:]
			#传入birthday列表中
			birthday.append(birthday_full)
			birthday.append(birthday_last_six)
			birthday.append(birthday_last_four)
		#无年份0523
		elif len(args.birthday) == 4:
			#form3-生日后四位
			birthday_last_four = birthday_tmp
			birthday.append(birthday_last_four)
		else:
			print(ERROR_TIPS + "输入生日格式错误！")
			sys.exit()
	else:
		birthday = ""

	#处理参数-邮箱
	mail = []
	if args.mail:
		mail_tmp = args.mail
		if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',mail_tmp):
			#form1-mail前缀
			mail_prefix = mail_tmp[:mail_tmp.find('@')]
			mail.append(mail_prefix)
		else:
			print(ERROR_TIPS + "输入邮箱格式错误！")
			sys.exit()
	else:
		mail = ""

	#处理参数-qq
	qq = []
	if args.qq:
		if args.qq.isnumeric():
			qq.append(args.qq)
		else:
			print("输入qq错误！")
			sys.exit()
	else:
		qq = ""

	args_list.append(username)
	args_list.append(password)
	args_list.append(cname)
	args_list.append(ename)
	args_list.append(tel)
	args_list.append(idcard)
	args_list.append(birthday)
	args_list.append(mail)
	args_list.append(qq)
	# print(args_list)
	return args_list

#func将命令行参数传给实例对象
def pass_args_list(person, commmand_args_list):
	args_list = []
	args_list = get_args()
	person.username = args_list[0]
	person.password = args_list[1]
	person.cname = args_list[2]
	person.ename = args_list[3]
	person.tel = args_list[4]
	person.idcard = args_list[5]
	person.birthday = args_list[6]
	person.mail = args_list[7]
	person.qq = args_list[8]
	return person

'''
一阶密码：仅根据一项个人信息生成的密码

二阶密码：根据两项个人信息组合生成的密码,去除低于六位的密码

三阶密码：由于部分人喜欢在两项个人信息中间加入一个特殊符号，以加强密码复杂度和强度，
为了包含这种情况，故根据两项个人信息以及一个常用的连接符号（默认：.!_-#@:$&*~?%+=/|，
建议尽量减少连接符，否则会极大增加密码数量，甚至导致内存溢出从而生成失败）生成三阶密码
'''

#func生成一阶密码字典
'''
测试语句
python3 test.py --level 1 -u twodog -p 123456 -cn 李二狗 -en Bill -t 17324001599 -id 441900199807161677 -b 19990526 -m tattoo123@qq.com -q 372335586

'''
def gendict_rank_one(person):
	password_list = []
	total = 0
	#打开弱组合文件，返回列表
	with open('weakdict.txt') as weakdict:
		weaklist = weakdict.read().splitlines()
	# print(weaklist)

	password_dict = open(u"一阶字典.txt","w+")
	#遍历对象属性
	for attr in dir(person):
		#将__开头的属性去除
		if attr[:2] != '__':
			#遍历每个属性的列表值
			for attr_list in getattr(person,attr):
				if attr_list != ',':
					#若该属性只有一个值，则直接存入，跳出循环
					if len(attr_list) == 1:
						password_list.append(getattr(person,attr))
						password_dict.write(str(getattr(person,attr))+'\n')
						total += 1
						break
					password_list.append(attr_list)
					password_dict.write(str(attr_list)+'\n')
					total += 1
	# print(password_list)
	#组合两项个人信息
	for i in range(len(password_list)):
		#分别在两项个人信息之间和后面加入特殊字符列表中的一个字符
		for w in range(len(weaklist)):
			password_dict.write(password_list[i] + weaklist[w] + '\n')
			total += 1

	print("一阶字典共生成{}项密码".format(total))
	password_dict.close()

#func生成二阶密码字典
'''
测试语句
python3 test.py -u twodog -p 123456 -cn 李二狗 -en Bill -t 17324001599 -id 441900199807161677 -b 19990526 -m tattoo123@qq.com -q 372335586 --level 2

'''
def gendict_rank_two(person):
	password_list = []
	password_dict = open(u"二阶字典.txt","w+")
	total = 0
	#遍历对象属性
	for attr in dir(person):
		#将__开头的属性去除
		if attr[:2] != '__':
			#遍历每个属性的列表值
			for attr_list in getattr(person,attr):
				if attr_list != ',':
					#若该属性只有一个值，则直接存入，跳出循环
					if len(attr_list) == 1:
						password_list.append(getattr(person,attr))
						break
					password_list.append(attr_list)
	#组合两项个人信息
	for i in range(len(password_list)):
		#枚举列表，获取索引，一定要有value，否则报错
		for index, value in enumerate(password_list):
			# print(password_list[i] + password_list[index])
			password_dict.write(password_list[i] + password_list[index] + '\n')
			total += 1
	print("二阶字典共生成{}项密码".format(total))
	password_dict.close()

#func生成三阶密码字典
'''
三阶字典生成含有特殊字符的字典，在两项个人信息的中间和后面添加特殊符号
测试语句
python3 test.py -u twodog -p 123456 -cn 李二狗 -en Bill -t 17324001599 -id 441900199807161677 -b 19990526 -m tattoo123@qq.com -q 372335586 --level 3

'''
def gendict_rank_three(person):
	#定义特殊符号列表
	special_char = ['.','!','_','-','#','@',':','$','&','*','~','?','%','+','=','/','|']	#17个
	password_list = []
	password_dict = open(u"三阶字典.txt","w+")
	total = 0
	#遍历对象属性
	for attr in dir(person):
		#将__开头的属性去除
		if attr[:2] != '__':
			#遍历每个属性的列表值
			for attr_list in getattr(person,attr):
				if attr_list != ',':
					#若该属性只有一个值，则直接存入，跳出循环
					if len(attr_list) == 1:
						password_list.append(getattr(person,attr))
						break
					password_list.append(attr_list)
	# print(password_list)
	#组合两项个人信息
	for i in range(len(password_list)):
		#枚举列表，获取索引，一定要有value，否则报错
		for index, value in enumerate(password_list):
			# print(password_list[i] + password_list[index])
			#分别在两项个人信息之间和后面加入特殊字符列表中的一个字符
			for sc in range(len(special_char)):
				password_dict.write(password_list[i] + special_char[sc] + password_list[index] + '\n')
				password_dict.write(password_list[i] + password_list[index] + special_char[sc] + '\n')
				total += 1
	print("三阶字典共生成{}项密码".format(total))
	password_dict.close()

#调用主函数
if __name__ == "__main__":
    str_pic()
    #命令行参数函数
    args = parse_args()
    # print(args)

    #获取命令行参数
    #实例化Person
    person = Person()
    #获取命令行参数，并赋给对象
    pass_args_list(person,get_args())

    #测试语句-输入各个信息的分割形式
    # print("username:{}".format(person.username))
    # print("password:{}".format(person.password))
    # print("cname:{}".format(person.cname))
    # print("ename:{}".format(person.ename))
    # print("tel:{}".format(person.tel))
    # print("idcard:{}".format(person.idcard))
    # print("birthday:{}".format(person.birthday))
    # print("mail:{}".format(person.mail))
    # print("qq:{}".format(person.qq))

    #生成密码字典
    # print(get_abbreviation(u"李二狗"))   #后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

    if args.level == 1:
        #一阶密码：仅根据一项个人信息生成的密码
        print("一阶字典" + PROCESS)
        gendict_rank_one(person)
    elif args.level == 2:
        #二阶密码：根据两项个人信息组合生成的密码
        print("二阶字典" + PROCESS)
        gendict_rank_two(person)
    elif args.level == 3:
        #三阶密码：二阶基础上，在两项个人信息中间或后面加入一个特殊字符
        print("三阶字典" + PROCESS)
        gendict_rank_three(person)