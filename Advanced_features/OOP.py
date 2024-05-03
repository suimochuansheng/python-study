"""
封装：将数据（属性）和行为（方法）打包在单一的工作单元中，即类。这有助于隐藏内部实现的细节，并且只暴露有限的接口与外界交互。

抽象：提取对象共同的特性，形成类的设计，这样可以忽略那些不重要的细节，专注于概念层面的设计。

继承：允许新创建的类（子类）继承现有类（父类）的属性和方法，便于代码重用并可以实现层次关系。

多态：允许子类通过继承得到与父类相同的方法名称，但是可以有不同的实现，这意味着同一个方法调用可以产生不同的行为。

"""


# 定义一个基础的类 Animal
class Animal:
    def __init__(self, name):  # 封装：通过初始化方法设置属性
        self.name = name  # 属性

    def speak(self):  # 抽象方法
        raise NotImplementedError("Subclass must implement abstract method")


# 继承Animal类，创建Dog类
class Dog(Animal):
    def speak(self):  # 多态：实现抽象方法
        return "Woof!"


# 继承Animal类，创建Cat类
class Cat(Animal):
    def speak(self):  # 多态：实现抽象方法
        return "Meow!"


# 使用
my_dog = Dog("Buddy")
print(f"{my_dog.name}: {my_dog.speak()}")  # 输出: Buddy: Woof!

my_cat = Cat("Kitty")
print(f"{my_cat.name}: {my_cat.speak()}")  # 输出: Kitty: Meow!
