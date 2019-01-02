import os
import time
print(os.name)
#print(os.environ)
#print(os.environ.get('PATH'))

#查看绝对路径
print(os.path.abspath('.'))
#在某个目录下新建目录
s=os.path.join('D:\GIS_Design_Department\git\pythonStudy\senior3','test')
print(s)
#os.mkdir(s)
#删除目录
time.sleep(2)
#os.rmdir(s)
#拆分路径 用split别用手动拆分，系统不同分隔符不同
print(os.path.split(s))
#拆分得到扩展名
print(os.path.splitext(s))
#文件重命名
#os.rename(os.path.join(s,'test1.txt'),'test1.py')
#查看当前目录下所有目录
a=[x for x in os.listdir('.') if os.path.isdir(x)]
print(a)
#查看当前目录下所有py后缀的文件
b=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(b)