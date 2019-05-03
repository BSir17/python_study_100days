#面向对象编程

#   @property装饰器
#我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
# 我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问
#那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作
#可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

#Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法
#动态语言允许我们在程序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属性和方法进行解绑定
#如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过在类中定义__slots__变量来进行限定
#需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
class Person_slots(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    person._other="ad"                      #给person加属性是可以加上的
    person1=Person_slots('Jack',13)
    person1._gender="male"
    person1._other="ad"                     #给person1加入slots外的属性则会报错
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()












