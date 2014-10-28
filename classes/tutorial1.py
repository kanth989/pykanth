# lets start programming to learn various things in python

# Funtions -- beginning

'''
Indentation or leaving trails of white spaces is essential in python
as loops, functions, classes and conditions are identified by 
white spaces; This is by avoiding curly 
braces used in C, C++ and many other languages
Essential-- Inorder to start a loop, function, class or condition simply
denote by placing a ':' at the end indicating that is the start of the respective.
To come out of it jsut move back to the respective margin.
'''

'''
Now we shall define Methods 
in Python with some code. Lets perform factorial 

'def' Keyword to declare a function/method followed by a name along with paranthesis to it.
Inside paranthesis we can pass any number of arguments or none depending upon the requiremet.
Lets see How it works.
'''

def factorial(a): # here a is an argument that is needed inorder to perform factorial
	if a == 0 or a==1: # this is a if condition to return 1 if the argument passed is less than 2
		return 1       # 'return' Keyword used to pass the value executed by the funtion when called
	else:  # moved the else back to the ('if' loop) margin same where the if is placed to process the condition above
		result = a*factorial(a-1) # Boom!! we performed factorial using recurssive call. 
		return result             # A recurssive call is calling the same function with in the function
		
print factorial(1) # check for factorial of one
print factorial(0) # check for factorial of zero
print factorial(6) # This the way to call the function

'''
'print' keyword is used to print the result
returned from the function 'factorial'
'''

# Functions -- intermediate
def testing_arguments1(*args, **kwargs):
	'''
	Python always stores the program in the form of 
	dictionaries (a data structure simply a way of storing in key value pairs)
	lets look into key value pairs by executing this function 'testing_arguments'
	'''
	print args, kwargs
print 'Testing argumetns 1'
testing_arguments1(1,2,3,4,5, val1=3, val2=5, val3=5) # execute this step to see the difference

# result of the testing_arguments
# (1, 2, 3, 4, 5) {'val3': 5, 'val2': 5, 'val1': 3}
# the above (1,2,3,4,5) are placed in tuple, an immutable or unbreakable data-structure
# that means you cannot break the data ones it is tuple but one can access the data in it, 
# and the rest is placed in dictionary, a value in dictionary can be called by the key directly 

def testing_arguments2(*args, **kwargs): # *args means arguments ;  **kwargs means key word arguments
	'''
	Now lets look into the arguments
	that are been passed to this fuction
	'''
	print args[2] # here the 2 is the index or location of the value in tuple starting from first element 
				# Note that first element is always indexed as 0 and rest 1,2,3 and so on
	print args[-3] # another way of calling a data in tuple '-' indicates to start counting from last element
				# Note that last element is always indexed as -1 and rest -2,-3 and so on	
	print kwargs['val2'] # Here we are trying to get the key val2 from the dictionary by calling the key directly
	print kwargs.get('val2') # Another way of calling dictionary, more pythonic way/
	print kwargs.get('val5', 100) # Here val5 is not sent as an argument. 
						#  But if val5 is not found then 100 will be assigned to it

print 'Testing argumetns 2  to see how python treats args and kwargs'
testing_arguments2(1,2,3,4,5, val1=3, val2=5, val3=5) # execute this step to see the difference

#Result 
# 3
# 3
# 5
# 5
# 100
print "Testing arguments 2 passing val5"
testing_arguments2(1,2,3,4,5, val1=3, val2=5, val3=5, val5=34) # passing val5 to the function; execute to see the diff

#Result 
# 3
# 3
# 5
# 5
# 34

'''
Obeservation:
No need to specify the data type of any variable at any time;
 Python is loosely typed that means that interpreter will understand the type of variable
 Lets check that 
'''
 

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
	



