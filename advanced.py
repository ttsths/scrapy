# _*_ coding: utf-8 _*_
import datetime
import json
from functools import reduce
from contextlib import contextmanager

from flask import Flask

print(list(range(1,5)))
## 推导式
list3 = [num for num in range(1,5) if num % 2 == 1]
print(list3)

world = "letter"
counts = {letter: world.count(letter) for letter in world}
print(counts)


d = {
	"a":"b",
	"c":"d"
}

d_result = {value: key for key, value in d.items()}
print(d_result)


"""
切片
前闭后开区间
"""
l = list(range(1,100))
print(l[:3])
print(l[80:])

"""
匿名函数
不支持return
"""

f = lambda a: a*a
print(f(2))

"""
高阶函数
"""
"""
 map()
 接收一个函数f和list，并把函数作用在这个list上
"""
def f(x):
	return x*x

mapList = list(map(f,[1,2,3]))
print(mapList)


"""
reduce()
f必须接受两个函数，对list的每个元素调用f
"""
def f1(x,y):
	return x*y

# = 1*2*3*4
list5 = reduce(f1,[1,2,3,4])
print(list5)


"""
filter()
过滤一些元素
"""
def is_odd(x):
	return x % 2 == 1

print(filter(is_odd, [1,2,3]))

"""
sort()
"""
list6 = [0,1,3,2,4,7,4,32,55]
print(sorted(list6))
print(sorted(list6,reverse = True))


"""
[
'  *  '
' *** '
'*****'
]
"""
def build_tower(m):
	return list(map(lambda x: ("*"*(2*x+1)).center(2*m-1),range(0,m)))
print(build_tower(3))

"""
1071225 = n^3+(n-1)^3+...+1^3
"""
def add(x,y):
	return x+y
def find_nb(m,n=0):
	while True:
		n +=1 
		r = reduce(add,map(lambda n:n**3,range(0,n)))
		print(r)
		if m == r:
			return n - 1
		elif r > m:
			 break
		return -1

print(find_nb(1))


"""
add(1)
add(1)(2)
add(1)(2)(3)

"""

class nextadd(int):
	def __call__(self,n):
		return nextadd(self+n)

next_result = nextadd(1)(2)(3);
print(next_result)


"""
深拷贝与浅拷贝
"""
import copy
alist = [1,2,3,[5,6],7]
## 浅拷贝
# blist = copy.copy(alist)
# alist[3].append("aaa")
# alist.append(7)
# blist.append(8)
# print(alist)
# print(blist)

## 深拷贝
blist = copy.deepcopy(alist)
alist[3].append("aaa")
alist.append(7)
blist.append(8)
print(alist)
print(blist)

"""
with
"""
def exercise():
	global f,content
	f = ""
	content = ""
	try:
		f = open("abc.txt","r")
		content = f.read()
	except Exception as e:
		print(e)
	finally:
		if f:
			f.close()
	return content

# exercise()


# with open("abc.txt", "r") as f:
# 	content = f.read()
# 	print(content)

class Agree:
	def __enter__(self):
		print("enter")
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("exit")
	def dosomething(self):
		print("do some thing")

with Agree() as agree:
	agree.dosomething()
"""
装饰器
运行之前就已经装饰
"""
@contextmanager
def open_file():
	print("opne file")
	yield {}
	print("end file")
with open_file() as open:
	print("file")

def deco(func):
	def inner():
		print("aaaa")
	return inner

@deco
def target():
	pass

target()

# app = Flask(__name__)
#
# @app.route("/")
# def hell():
# 	print("Hello World")
# 	return "Hello World"
#
# app.run()

list = []
def register(active = True):
	def decorator(func):
		print('running register(active=%s)->(%s)' %(active,func))
		if active:
			list.append(func)
		return func
	return decorator
"""
工厂方式的装饰器
"""
@register(active=True)
def f1():
	print("f1")

@register(active=True)
def f2():
	print("f2")

@register(active=False)
def f3():
	print("f3")

if __name__ == "__main__":
	print("list->",list)
	f1()
	f2()
	f3()

"""
属性描述符
"""
class Age(object):
	def __init__(self,value = 20):
		self.value = value

	def __get__(self, instance, owner):
		print("get --> obj:%s type: %s"%(instance, owner))
		return self.value

	def __set__(self, instance, value):
		print("__set__ --> obj:%s type: %s" % (instance, value))
		self.value = value

class Person(object):
	age = Age()
	def __init__(self, name):
		self.name = name
p = Person("申屠海三")
print(p.age)
p.age=25
print(p.age)

data = {
	"name": "demo",
	"age": 1
}


"""
对象序列化
需要提供serialize方法
"""
def person_serialize(obj):
	d = {'__classnmae__':type(obj).__name__}
	d.update(vars(obj))
	return d
person_str = json.dumps(p,default=person_serialize)
print(person_str)

## date to json
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
new_data = json.loads(json_str)
print(new_data["name"])

"""
迭代器
对象内部实现了迭代协议，这个对象就是一个迭代器
容器 tuple set dict
"""
list7 = [1,2,3,4]
print(1 in list7)
class A(object):
	def __init__(self):
		self.items = [1,2]

	def __contains__(self, item):
		return item in self.items

a = A()
print( 1 in a)

"""
可迭代对象不一定是迭代器
"""
class Worker(object):
	def __init__(self,n):
		self.n = n
		self.id = 0
	def __iter__(self):
		print("__iter__")
	def __next__(self):
		value = self.id
		self.id +=1
		# if self.id > self.n:
		# 	raise StopIteration
		return value

w = Worker(3)
for i in w:
	print(i)
