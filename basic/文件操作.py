"""使用os和shutil模块来对文件进行基本操作"""
import time

"""对文件读取、写入和添加内容"""
# 以读模式打开一个文件
with open('../tools/example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 以写模式打开一个文件（如果文件不存在，会创建文件），如果文件有内容，会覆盖原内容写入新内容
with open('../tools/newfile.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!')

# 逐行读取文件内容
with open('../tools/example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

# 向文件追加文本,使用“a”模式添加-add
with open('../tools/newfile.txt', 'a', encoding='utf-8') as file:
    file.write('\nThis is added text.')



"""获取文件属性"""
# 获取文件大小
import os

size = os.path.getsize('../tools/example.txt')

# 检查文件是否存在
if os.path.exists('../tools/example.txt'):
    print('File exists')
else:
    print('File does not exist')

# 获取文件最后修改时间
file_path = "../tools/example.txt"
mtime_timestamp = os.path.getmtime(file_path)
# 转换成本地时间
st_time = time.localtime(mtime_timestamp)
# 修改时间为格式化字符串
str_time = time.strftime('%Y-%m-%d %H:%M:%S', st_time)
# print(str_time)


"""文件和目录的复制、移动和删除"""
import shutil

# 复制文件
# shutil.copy('source.txt', 'destination.txt')
#
# # 移动文件
# shutil.move('source.txt', 'destination.txt')
#
# # 删除文件
# os.remove('example.txt')

# 删除目录及其所有内容
# shutil.rmtree('../basic/aaa')

"""列出目录内容"""
# 列出当前工作目录下的所有文件和目录
import os
for item in os.listdir():
    # print(item)
    pass

# 仅列出当前工作目录下的所有目录
for item in os.listdir():
    if os.path.isdir(item):
        # print(item)
        pass

# 列表当前工作目录下的所有文件
for item in os.listdir():
    if os.path.isfile(item):
        # print(item)
        pass


"""numpy操作文件方式"""
# 读取文本文件
import numpy as np
data = np.loadtxt('../tools/aaa.txt', delimiter=',')

