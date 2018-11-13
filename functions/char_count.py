def count_char(string, char):
	""" Find the number of occurrence of the passed character agument
		from the passed string argument. Function returns the count 
		of the character in the given string, if the characters is 
		not found returns -1.

        Args:
            string: It sould be a string data type from which need to find
					the number of occurrence of character.
            char: It should be a character data type.

        Returns:
            Returns the number of occurrence of the character in 
			the given string. If the character is not found in the string
			returns -1.
    """

	value = string.count(char)
	if (value):
		return value
	else :
		return -1
  
string = input("Enter a string : ")
char = input("Enter a character to be found in the string : ")
return_val = count_char(string,char)
if (return_val == -1):
	print ("Character is not found in the string")
else :
	print ("Count of given character occurrence in the string is", return_val)

