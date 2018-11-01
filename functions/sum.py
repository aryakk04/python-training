def sum_arguments (arg1,arg2):
	""" Prints the sum of passed two argument
		Two arguments should be either integer or string data type.
		If both arguments are either integer or string 
		return the sum of the arguments else return -1.

		Args:
			input1:  Argument 1 sould be either integer or string.
			input2:  Argument 2 should be either integer or string.
			Two arguments should be either string or integer data type.

		Returns:
			If two arguments are either integer or string return
			value is sum of two arguments else return value is -1.
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
