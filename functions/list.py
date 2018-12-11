#!/usr/bin/python

def get_system_to_ip_map(list1,list2,number):
	""" Get lists of system names and system IPs
		then prints the list of tuple which has system name 
		and corresponding system IP.
		
		Args:
			list1:  It is list of system names.
			list2:  It is list of system IPs
			number: It is the number of systems to be entered

        Returns:
            Returns list of tuple having system name and 
			corresponding system IP.
    """

	list3 = []
	for x in range (0,number):
		list3 += [(list1[x],list2[x])]
	return list3

number = input("Enter the number of systems : ")
list = raw_input("Enter system names seperated by coma : ")
list1 = list.split(',')
list = raw_input("Enter system IPs seperated by coma : ")
list2 = list.split(',')
list3 = get_system_to_ip_map(list1,list2,number)
print list3

