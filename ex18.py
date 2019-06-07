#introduction to functions


#this function takes arguements 'args', amount of args is defined inside the function, and prints the two arguements
def print_two(*args): 
	arg1,arg2 = args 
	print" arg1: %r, arg2: %r " % (arg1,arg2)

#this function is the same as previous, though we defined the amount of arguments in the function parameters
def print_two_again(arg1,arg2):
		print" arg1: %r, arg2: %r" % (arg1,arg2)
#function prints one arguement
def print_one(arg1):
			print "arg1: %r" % arg1
#function prints the sentence when called
def print_none():
			print("I have nothing.")

print "Give me two names:" #prompt for two names

input1 = raw_input(":")
input2 = raw_input(":")

#calling on each function with arguments given by user
print_two(input1,input2)
print_two_again(input1,input2)
print_one(input1)
print_none()


