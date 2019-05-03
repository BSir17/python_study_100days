a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)                           #对结果进行向下取整
print(a % b)
print(a ** b)                           #a的b次方
print("----------------------")

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True                               #使用type查看变量类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#练习1：华氏温度转摄氏温度。
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print("%.1f huashi ,and sheshi %.1f" % (f, c))             #格式化的输入输出




