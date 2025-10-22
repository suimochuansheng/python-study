# 一，列表
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 1.1 下标位输出
# print( list[0] )
# print( list[1] )
# print( list[2] )

# 1.2 切片输出--包含开始位，不包含结束位
# print( list[0:3] )
# print( list[1:4] )
# print( list[2:] )
# print( list[:3] )

# 1.3 倒序/间隔取值
# 1.3.1步长输出--默认步长为1，也可以自定义步长
# print( list[5::-2] ) 
# print( list[1:5:2] )
# print( list[2:5:2] )
# print( list[3:5:2] )
# print(list[::-1]) # 倒序输出
# print(list[0:6:2]) # 从0开始，每隔2个取一个，间隔2是包括左侧的元素

# 1.3.2容易忽略的点
# 当步长为负数时( list[start:end:step] )：
# - 省略 start 参数时，默认值为 -1 （列表最后一个元素）
# - 省略 end 参数时，默认值为 -len(list)-1 （列表第一个元素之前）
# print( list[::-2] ) == print( list[-1:-7:-2] ) 
# print( list[::-2] ) # >>> ['black', 'yellow', 'green']
# print( list[5::-2] ) # >>> ['black', 'yellow', 'green']

# 这里步长多大都么用，因为只有0下标一个元素，从0开始倒序取值，所以只有一个元素
# print( list[0::-2] ) # ['red']

# 1.4 



# 元组


# 字典


# 集合



#数字，字符串，布尔值