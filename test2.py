import argparse
import sys
def parse_args():
  parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -u username [options...]")

  #gendict
  gendict = parser.add_argument_group('gendict')
  gendict.add_argument("--level",type=int,choices=[1,2,3],help="[REQUIRED]the level of dict",required=True)
  gendict.add_argument("-u","--username",type=str)
  gendict.add_argument("-p","--password",type=str)
  gendict.add_argument("-cn","--cname",type=str)
  gendict.add_argument("-en","--ename",type=str)
  gendict.add_argument("-t","--tel",type=str)
  gendict.add_argument("-id","--idcard",type=str)
  gendict.add_argument("-b","--birthday",help='Example: 19990523 or 0523')
  gendict.add_argument("-m","--mail",type=str)
  gendict.add_argument("-q","--qq",type=str)


  #yanzhengma
  yzm = parser.add_argument_group('yzm')
  yzm.add_argument('--ocr',action = "store")

  #intruder
  intruder = parser.add_argument_group('intruder')
  intruder.add_argument('--intruder',action="store")

  # parser.add_argument('--push', action='store')
  return parser.parse_args(['-h'])

if __name__ == "__main__":
    #命令行参数函数
    args = parse_args()
