"""
装饰器：装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
装饰器通过在函数上方添加@decorator_name来实现装饰器效果。

应用场景：
日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
性能分析: 可以使用装饰器来测量函数的执行时间。
权限控制: 装饰器可用于限制对某些函数的访问权限。
缓存: 装饰器可用于实现函数结果的缓存，以提高性能。

"""


# 基础用法
# Python 装饰允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# 使用装饰器装饰一个函数
@my_decorator
def say_hello():
    print("Hello, World!")


# @my_decorator添加在say_hello函数上时，将say_hello函数当做参数传递进装饰器my_decorator中，并运行wrapper函数

# 调用
# say_hello()


"""==============================================================================================================="""


# 装饰器带参数用法
# 以下方法中n代表着装饰器要执行几次
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # _ 占位符，此处循环用法表示不打算在循环体内使用它的值，可以节省一定内存空间
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")

"""==============================================================================================================="""


# 类装饰器
# 类装饰器是一种特殊的装饰器，它用于修改类。类装饰器在Python中经常用于扩展或修改类的行为，而不需要直接修改原始类
def class_decorator(cls):
    # 在装饰器内部对类进行修改
    cls.extra_attribute = "这是额外的属性"

    # 返回修改后的类
    return cls


# 使用 @ 符号将装饰器应用到一个类上
@class_decorator
class MyClass:
    def __init__(self):
        self.attribute = "原始属性"


# 创建 MyClass 的实例
my_instance = MyClass()

# 访问原始属性和新添加的属性
print(my_instance.attribute)  # 输出: 原始属性
print(my_instance.extra_attribute)  # 输出: 这是额外的属性

"""==============================================================================================================="""
"""
常见的装饰器及用法

"""
print("*" * 50)
import functools
import time
import logging

# 设置基本的日志配置,简单的配置工具，它可以设置日志的级别、格式、输出目标等,日志级别为logging.INFO，意味着只有信息级别及以上的日志消息会被显示
logging.basicConfig(level=logging.INFO)


# 创建一个日志记录装饰器
def logger(func):
    # @functools.wraps(func)会保存函数的名称__name__和文档字符串信息__doc__
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        logging.info(f"这是文档字符串内容：{func.__doc__}")
        # 执行传入的函数
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned： {result}")
        return result

    return wrapper


# 创建一个计时装饰器
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 使用 time.perf_counter() 来获取当前的时间戳,返回值通常是秒的小数部分，其精度取决于系统的硬件和操作系统。
        # 通过start_time和end_time的差值计算函数执行的时间
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(start_time, "/", end_time)
        # :.4f 控制函数执行时间的小数点后只显示4位
        logging.info(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


# 使用装饰器
@logger
@timer
def add(x, y):
    """文档字符串描述：Add two numbers."""
    return x + y


# 调用函数
add(1, 2)

"""==============================================================================================================="""
# 性能分析装饰器
# timeit：这是Python标准库中的一个装饰器，用于测量小段代码的执行时间。它有助于比较不同代码片段的性能。
from timeit import timeit


@timeit
def my_function():
    # 在这里放置你的代码
    pass


# cProfile：这是另一个Python标准库中的工具，它提供了更详细的性能分析，包括函数调用次数、每一次调用的耗时、累积时间等。
import cProfile


def my_function():
    # 在这里放置你的代码
    pass


cProfile.run('my_function()')
# profile：这是cProfile的一个简单装饰器，它可以直接在函数上使用，打印出性能分析结果。
from profile import profile


@profile
def my_function():
    # 在这里放置你的代码
    pass


# line_profiler：这是一个第三方库，它可以提供更细粒度的性能分析，包括每行代码的执行次数和耗时。
from line_profiler import LineProfiler

lp = LineProfiler()


def my_function():
    # 在这里放置你的代码
    pass


lp_wrapper = lp(my_function)
lp_wrapper()
lp.print_stats()

# memory_profiler：这是另一个第三方库，用于监控函数的内存使用情况。
from memory_profiler import profile


@profile
def my_function():
    # 在这里放置你的代码
    pass


"""==============================================================================================================="""
# 文档读取装饰器
# 验证文件存在的装饰器：
import os


def ensure_file_exists(func):
    def wrapper(file_path, *args, **kwargs):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        return func(file_path, *args, **kwargs)

    return wrapper


@ensure_file_exists
def read_document(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# 记录操作日志的装饰器：这个装饰器会在读取文档之前和之后记录日志信息。
import logging


def log_operation(func):
    def wrapper(file_path, *args, **kwargs):
        logging.info(f"正在读取文件: {file_path}")
        result = func(file_path, *args, **kwargs)
        logging.info(f"文件读取完成: {file_path}")
        return result

    return wrapper


@log_operation
def read_document(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# 格式化文档内容的装饰器：这个装饰器会在读取文档之后对内容进行格式化，例如去除空白字符并将所有字母转换为大写。
def format_document(func):
    def wrapper(file_path, *args, **kwargs):
        content = func(file_path, *args, **kwargs)
        # 假设这里有一些格式化内容的逻辑
        formatted_content = content.strip().upper()
        return formatted_content
    return wrapper

@format_document
def read_document(file_path):
    with open(file_path, 'r') as file:
        return file.read()