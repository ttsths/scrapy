"""
寻找最长不重复字符串的个数
"" 0
a  1
asdf 4
asdavfg 6
"""
# _*_ coding:utf-8 _*_
def non_repeating(s):
	start = 0
	maxLength = 0
	d = dict()
	for key,value in enumerate(s):
		## none 0 
		print(key)
		print(value)
		print(d.get(value))
		if d.get(value):
			print(key)
		if d.get(value) == 0 or d.get(value):
			start += 1
		elif key-start+1 > maxLength:
			maxLength = key-start+1
		print (start)
		d[value] = key
		print(d)
	return maxLength

# print(non_repeating("a"))
# print(non_repeating("asdaafg"))
# print(non_repeating("侯情情"))
print(non_repeating("在干嘛在今天过得好慢"))

"""
字符编码
ascii 
"""