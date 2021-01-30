
class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade


	def get_grade(self):
		return self.grade


class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)


class Pet:
	def __init__(self, name, age):
		self.names = name
		self.age = age

	def show(self):
		print(f'I am {self.names} and I am {self.age} years old')

class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age)
		self.color = color

	def speak(self):
		print('meow')

	def show(self):
		print(f'I am {self.names} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
	def speak(self):
		print('bark')

##

s1 = Student('tim', 19, 95)
s2 = Student('bill', 19, 75)
s3 = Student('jill', 19, 65)

course = Course('science', 2)
course.add_student(s1)
course.add_student(s2)
#print(course.add_student(s3))
#print(course.get_average_grade())


## 

p = Pet('tim', 19)
p.show()

c = Cat('bill', 34, 'brown')
d = Dog('jill', 25)
c.show()
c.speak()

d.show()
d.speak()

