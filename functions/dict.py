def char_dict (string):
	""" Prints the dictionary which has the count of
		each character occurrence in the passed string
		argument

        Args:
            String:  It sould be a string from which character
			occurrence will be counted.

        Returns:
			Returns dictionary having count of each character
			in the given string.
    """
	char_dic = {}
	for char in string:
		if char not in char_dic:
			char_dic[char] = string.count(char)
	return char_dic

string = input("Enter a string : ")
char_dic = char_dict (string)
print (char_dic)
