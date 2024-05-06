"""
迭代器与生成器:
迭代器：迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()，分别是创建迭代器对象和输出迭代器下一个元素。

"""
import time

# 迭代器示例代码
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

while True:
    try:
        element = next(iterator)
        time.sleep(1)
        print(element)
    except StopIteration:
        break