import sys
from yzm import OCR
'''
测试语句
python3 main.py http://www.isaipu.net/common/image.jsp
'''
print(OCR(sys.argv[1:][0]))