def sum_arguments (arg1,arg2):
	""" Prints the sum of passed two argument
		if both arguments have the same data type.

		Args:
			arg1:  Any value
			arg2:  Any value

		Returns:
			sum of arguments or if both argument have
			different data types return value is -1.
	"""

	if (type(arg1) != type(arg2)): 
	# Since types of arguments are not same
		return -1
	else:
		sumarg = arg1+arg2
		return sumarg

input1 = input("Enter input1 : ")
input2 = input("Enter input2 : ")

return_val = sum_arguments (input1, input2) 
# Function calling to find the sum of arguments
if (return_val == -1) :
	print ("Both inputs should have the same data type")
else:
      print "sum of two argument", return_val
