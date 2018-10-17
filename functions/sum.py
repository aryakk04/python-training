## Function to find the sum of arguments

def sum_arguments (arg1,arg2):
	if (type(arg1) != type(arg2)): 
	# Since types of arguments are not same
		return -1
	else:
		sumarg = arg1+arg2
		print ("Sum of arguments is: ", sumarg)
		return 1

input1 = input("Enter input1 : ")
input2 = input("Enter input2 : ")

return_val = sum_arguments (input1, input2) 
# Function calling to find the sum of arguments
if (return_val == -1) :
	print ("Both inputs should have the same data type")

