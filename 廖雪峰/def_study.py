#
# 函数第二章:定义函数
#

#自定义abs函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#参数个数不匹配，会抛出TypeError
#my_abs(1,2)

'''
    完善my_abs函数
    isinstance()为检查数据类型的内置函数
'''
def my_abs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#返回多个值的函数
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#只能返回一个值
x, y = move(100, 100, 60, math.pi/6)
print(x, y)

#返回一个tuple(元组)
r = move(100, 100, 60, math.pi/6)
print(r)


def nop():
    ''' 
        pass是占位符
        如果一个函数声明后不想放置代码
        不可像JS一样置空
        必须写入此关键字
        否则会报语法错误
        判断语句同理
    '''
    pass

'''
小结：
    定义函数时，需要确定函数名和参数个数
    如果有必要，可以对参数的数据类型做检查
    函数体内部可以用 return 随时返回函数结果
    函数执行完毕也没有 return 语句时，自动 return None
    函数可以同时返回多个值，但其实就是一个 tuple
'''

'''
练习：
    请定义一个函数quadratic(a, b, c), 接收3个参数，返回一元二次方程
    ax^2 + bx + c = 0 的两个解
提示：
    可使用公式法
    计算平方根可以调用 math.sqrt() 函数
'''

import math
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    return x1, x2

r = quadratic(2, 3, 1)
print(r)

#
# 函数第三章:函数的参数
#

#写一个计算x平方的函数
def power (x):
    return x*x

#写一个计算x的n次方的函数
def power_n (x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

power_n(2, 30)

#但是给power()函数传入第二个参数就会报错
#原因是power()函数只支持一个参数
#因为我们经常计算x的平方
#所以可以给power_n()函数设置默认参数

def power_defult (x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

#这样当power_defult()函数只传入一个参数时
#则默认计算x的平方

#注意:默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L

add_end([1, 2, 3])
#[1, 2, 3, 'END']

add_end(['x', 'y', 'z'])
#['x', 'y', 'z', 'END']

add_end()
#['END', 'END']
add_end()
#['END', 'END', 'END']

#因为在python函数定义的时候，默认参数 L 的值就被计算出来了
#即 [] ，因为默认参数 L 也是一个变量，它指向对象 []
#每次调用add_end()函数，如果改变了 L 的内容
#则下次调用时，默认参数的内容就变了，不再是函数定义时的 [] 了

#修改:可使用None这个不变对象来实现
def add_end2 (L=None):
    if L is None:
        L = []
        L.append('END')
    return L

'''
#设计不变对象的原因:
    因为不变对象一旦创建，对象内部的数据就不能修改
    这样就减少了由于修改数据导致的错误
    此外，由于对象不变，多环境下同时读取对象不需要加锁，同时读没有一点问题
    所以能设计不变对象时，优先设计不变对象
'''

#可变参数
#在python中，还可以定义可变参数，即参数个数是可变的(类似JS的重载)
#由于参数个数不确定，我们一般首先需要想到把参数作为一个 list 或 tuple 传进来

def calc (numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#但是调用时，需要先组装出一个 list 或 tuple
calc([1, 2, 3])
calc((1, 3, 5, 7))

#利用可变参数
#定义时，仅需在参数前加一个 * ，在函数内部，参数numbers接收到的是一个tuple
#因此，函数代码完全不变，但是调用时可以传入任意数量的参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc2(1, 2, 3)
calc2(1, 3, 5, 7)

#如果已经有一个 list 或 tuple，要调用一个可用函数，可使用
nums = [1, 2, 3]
calc2(nums[0], nums[1], nums[2])
#太繁琐
#正确姿势
calc2(*nums)

#关键字参数