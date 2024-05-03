'''try except 用法'''

# 通用
try:
    # 尝试执行的代码
    result = 10 / 0
except ZeroDivisionError:
    # 如果发生了除以零的错误，则执行这个块
    print("You can't divide by zero!")
except Exception as e:
    # 处理除 ZeroDivisionError 外的所有异常
    print(f"An error occurred: {e}")
else:
    # 如果没有异常发生，则执行这个块
    print("Everything went well!")
finally:
    # 无论是否发生异常，都执行这个块
    print("The 'try except' is finished.")

"""======================================================================================="""

"""except 常见可捕获错误类型"""

# ValueError：当传递了一个错误的值时引发，例如尝试将字符串转换为整数时
try:
    num = int("not a number")
except ValueError:
    print("That's not a valid number!")

# TypeError：当对不适当类型的对象执行操作时引发
try:
    num = 10 + "five"
except TypeError:
    print("Can't add integer and string together!")

# NameError：当尝试访问一个未定义的变量时引发
try:
    print(undefined_variable)
except NameError:
    print("That variable is not defined yet!")

# IndexError：当尝试访问序列（如列表、元组、字符串）的索引超出范围时引发
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("List index out of range.")

# KeyError：当尝试访问字典中不存在的键时引发
try:
    my_dict = {"apple": "red", "banana": "yellow"}
    print(my_dict["cherry"])
except KeyError:
    print("That key does not exist in the dictionary.")

# ZeroDivisionError：当尝试将数字除以零时引发
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# FileNotFoundError：当尝试打开不存在的文件时引发
try:
    with open("nonexistent_file.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")

# IOError：当输入输出操作失败时引发
try:
    with open("some_file.txt", "w") as file:
        file.write("Some content")
except IOError:
    print("An error occurred while writing to the file.")

