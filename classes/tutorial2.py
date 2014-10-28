# Classes:  'class' Keyword is used to declare classes
class Sample1(): # This class is Old way of declaring class
	pass 		# 'pass' Keyword means do nothing ; Just skip after entering in a loop, condition, class or function

	
'''
comments can be of two types single line 
comment with '#' at beginning
and multiple line comments 
like this(can use single quotes of double quotes)	
any text editor will highlight the region of the comment
'''

class Sample2(object): # This is new way of declaring class 
	pass

# Let's see what is the difference between the Old way and new Way Later when we talk about MRO's 
# But for now we shall find how classes (New Way) can really help us.

# Lets Consider a real classroom full of students where each has a name , age , rollnumber
# Always take a class as classroom inorder to understand full conceppt of OOPs 
# I consider it as best way , all the examples provided here are completely to do with
# a real classroom  from a school packed with students, teachers, etc.. But do not limit yourself with this.
# Keep experimenting for a better learning.


'''
Little Intro about OOPs:

Real classroom has specific set of subjects to deal with so goes with
classes in OOPs but they are called as class-definitions or class-methods or class-functions
There will be fixed set of subjects for a given classroom. so does a class in OOPs , but 
they are declared using a constructor. We will talk about that in detail later
, here in python we declare a constructor using 
specific keyword '__init__' (double-underscore)
'''

class Student(object):       # Declaring a class;  
	school = 'Big School Name'  # variables declared outside of class-definitions are locally valid. 
	def __init__(self, name, age, rno): # Here is a constructor.
		self.name= name          # here we are assigning object values
		self.age = age
		self.rno = rno
	def print_details(self): # we always pass the 'self' to refer to the current object of the class
		print self.name + " Name of the Candidate" # Here we are performing string concatination
		print self.age, "Age of the Candidate" # here Integer value cannot concatinate with string
		print str(self.rno)+ " Roll Number of the Candidate" # here we are converting rno to string to perform string concatination

siva = Student('siva',18, 1090) # taking siva as Student Instance. An Instance is just a carrier.

print  siva.print_details()
print siva.age, siva.name,siva.rno, siva.school # here we are making use of constructor.
# but if i call school variable outside the class, python interpreter will throw error 
# try it
# print school

# Abvoe class Student does not do anything big
# Lets take a small situation where you asked each student to collect his/her teacher(s) name
# we shall see how it goes
class Student(object):
	school = "Big School Name"
	
	all_teachers= set() # here we are declaring a set, a data-structure that allows only unique values, unordered in nature
	def __init__(self, name, age, rno):
		self.name= name
		self.age = age
		self.rno = rno
		self.teachers = [] # here we are declaring a list; lists are similar to array, they are mutable and we can break and crack them as we wish.
	def add_teacher(self, Teacher):
		self.teachers.append(Teacher)
		self.all_teachers.add(Teacher)
	
# Here we are appending Teacher name provided by the class instance into 'teacher' list and 'all_teachers' set
# Observation: 
# 'teacher' list is declared in constructor making it only particular to an instance
# but 'all_teachers' set is declared as a local variable out of class-definitions making possible for all instances.

siva = Student('siva',18,1090)
seeta = Student('seeta',19,1192)
siva.add_teacher('Mr.Hanuman') # siva's  teachers
siva.add_teacher('Mr.Ravan')
seeta.add_teacher('Mr.Rama')  # seeta's teachers
seeta.add_teacher('Mr.Lakshman')
seeta.add_teacher('Mr.Hanuman') # Mr.Hanuman teahces for both seeta and siva 
print siva.teachers
print seeta.teachers
print siva.all_teachers  # calling local_variable 
print seeta.all_teachers  # But all teachers should have only one Mr.Hanuman

'''
Execute this program to see the result set 
'''

# This class is some what useful, But what is the case when i have to collect details from 100 schools.
# This is where Inheritance comes into the picture. A Big thing to worry is made simple by Inheritance.




