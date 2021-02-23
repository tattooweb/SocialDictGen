import argparse
import sys
def parse_args():
  parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u username [options...]")

  #gendict
  gendict = parser.add_argument_group('GEN_DICT')
  #level定义生成字典的阶数，必选参数，默认为1，只能输入1,2,3
  gendict.add_argument("--level",type=int,choices=[1,2,3],help="[REQUIRED]the level of dict")
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

def parse_args_help():
  parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u username [options...]")

  #gendict
  gendict = parser.add_argument_group('GEN_DICT')
  #level定义生成字典的阶数，必选参数，默认为1，只能输入1,2,3
  gendict.add_argument("--level",type=int,choices=[1,2,3],help="[REQUIRED]the level of dict")
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

if __name__ == "__main__":
    #命令行参数函数
    args = parse_args()
