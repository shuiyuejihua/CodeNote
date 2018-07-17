'''
学校成员类：
	person基本人员ADT
	student学生ADT
	staff教职工ADT
ADT Person:
	Person(self,strname,strsex,tuple birthday,strident)
	id(self)
	name(self)
	sex(self)
	birthday(self)
	age(self)
	set_name(self,strname)
	<(self,Person another)
	detail(self)

ADT Student(Person):
	Student(self,strname,strsex,tuple birthday,str department)
	department(self)
	en_year(self)
	scores(self)
	set_course(self,str course_name)
	set_socre(self,str course_name,int score)

ADT Staff(Person):
	Staff(self,strname,strsex,tuple birthday,tuple entry_date)
	department(self)
	salary(self)
	entry_date(self)
	position(self)
	set_salary(self,int amount)

'''

import datetime
class Person:
	"""docstring for Person"""
	_num = 0
	def __init__(self, name, sex, birthda, ident):
		if not (isinstance(name,str) and sex in('女','男')):
			raise PersonValueError(name, sex)
		try:
			birth = datetime.date(*birthday)
		except Exception as e:
			raise PersonValueError("Wrong date:",birthday)

		self.arg = arg
