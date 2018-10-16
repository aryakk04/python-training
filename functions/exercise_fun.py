## function to find the data type of passed arguments

def find_type_argument (number,number_two):
	try:
		val = int(number)
		print("Argument 1 is an intiger")
	except ValueError:
		try:
			val = float(number)
			print ("Argument 1 is a float number")
		except ValueError:
			print ("Argument 1 is a string")
	try:
		val = int(number_two)
		print("Argument two is an intiger")
	except ValueError:
		try:
			val = float(number_two)
			print ("Argument two is a float number")
		except ValueError:
			print ("Argument two is a string")
	return 1

##	Function to find the sum of integer or string inputs.
##	Two inputs should be either intiger or string.	
def sum_of_inputs (number,number_two):
	n1 = 0
	n2 = 0
	p1 = 0
	p2 = 0
	try:
		val = int(number)
	except ValueError:
		n1 = 1
		try:
			val = float(number)
		except ValueError:
			p1 = 1
	try:
		val_2 = int(number_two)
	except ValueError:
		n2 = 1
		try:
			val_2 = float(number_two)
		except ValueError:
			p2 = 1
	if (n1 != 1 and n2 != 1):
		# since both the conditions are true.
		sum_number = val + val_2
		print ("Sum of arguments : ", sum_number)
	elif(p1 == 1 and p2 == 1):
		# since bith the conditions are true.
		val = str(number)
		val_2 = str(number_two)
		sum_number = number + number_two
		print ("Sum of arguments  : ", sum_number)
	elif((n1 == 1 and n2 != 1) or (n1 !=1 and n2 == 1) or 
		(n1 == 1 and p1 != 1) or (n2 ==1 and p2 != 1)):
		# since all conditions are true.
		return -1

number = input ("Enter first argument : ")
number_two = input ("Enter second argument : ")
find_type_argument (number,number_two) ## Function calling to find the data type of arguments
ret = sum_of_inputs (number,number_two) ## Function calling to find the sum of arguments.
if ret == -1:
	print ("Two inputs should be either intiger or string")
