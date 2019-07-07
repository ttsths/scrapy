import requests
import random


# r = requests.get('https://api.github.com/events')
# content = r.text
# encoding = r.encoding
# # print(encoding)
# print(content)

l = ["java", "python", "golang"]
l[0]="C"
print(len(l))


"""
元祖 不可变 tuple
线程安全

"""
t = ("java", "python", "golang") 
print(t)
print(t[:3])

"""
dict 字典
key
   1,不可变 字符串 整数  bool 元祖

"""
d = {
	"NO1":"xm",
	"NO2":"xh",
	"NO3":"xy"
}
print(d["NO1"])
print("NO1" in d.keys())

"""
set 
不可重复
可以去重
"""
s = set(l)
print(s)
s1 = "ssssssssdwdwdw"
print(set(s1))

for index,x in enumerate(l):
	print('% s',index)

"""
def 函数
"""
print(random.randint(1, 10))

str = input("请输入字符串：").lower()
str1 = input("请输入另一个字符：").lower()

if str.isalnum() or " " in str:
	print(str.count(str1))
else:
	print('error')


b = (1,2,3,4,5)
print(list(b))

def find_index(arr):
	for i, k  in enumerate(arr):
		s = 0
		r = 0
		# 数组切片 从第i+1 个索引往后取
		for x in arr[i+1:]:
			s += x
		# 数组切片 从第0个索引往后取,不包括索引i的元素	
		for x in arr[:i]:
			r += x

		if s == r:
			return i
			break
	return -1

arr = [10,20,3,15,15]
print(find_index(arr))
print(arr[find_index(arr)])

"""
try:
except  Exception as e:
finally
"""
try:
	print("to do")
	a/0
except Exception as e:
	print(e)
finally:
	print('i am finally')

"""
主动抛出异常

"""
class customException(ValueError):
	pass

def make_error(a):
	n = int(a)
	if n == 0:
		raise customException("i am customException")
	return 1/n
make_error(0)