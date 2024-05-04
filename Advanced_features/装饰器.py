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
