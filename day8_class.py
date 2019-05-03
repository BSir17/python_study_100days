#类 这里讲的是封装
#day9继续
class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    #在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
    # 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__foo = "afoo"

    #方法也是私有 加两个下划线
    def __bar(self):
        print(self.__foo)
    def study(self, course_name):           #公有方法可以调用私有变量
        print('%s正在学习%s.' % (self.name, course_name))
        print(self.__foo)

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()
    #stu2.__bar()                       #不能调用

    #实际上还是可以访问到的，并没有限定死
    stu2._Student__bar()
    print(stu2._Student__foo)

#实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
# 所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
# 本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，
# 单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻

if __name__ == '__main__':
    main()

