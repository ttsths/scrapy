import datetime
class Student(object):
	num = 0
	def __init__(self,name,age,birthday):
		self.name = name
		self.age = age
		self.__birthday = birthday

	"""
	静态方法
	参数随意
	方法中不能使用类或者实例的任意属性和方法
	实例和类对象都可以哦调用
	"""
	@staticmethod
	def getTotalStu():
		print("staticmethod can not")
		pass




	"""
	类方法
	第一个参数必须是当前对象一般是cls
	通过它来传递类的属性和方法
	实例和类都可以调用
	"""
	@classmethod
	def s_plus(cls):
		cls.num += 1
		return cls.num

stu1 = Student("sths", 18, datetime.date(1994,6,9))
print(Student.s_plus())
print(Student.getTotalStu())
