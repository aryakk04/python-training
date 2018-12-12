#!/usr/bin/python

def get_system_to_ip_map(system_names,system_ips):
        """ Get lists of system names and system IPs
        then prints the list of tuple which has system name
        and corresponding system IP.

        Args:
            system_names:  It is list of system names.
            system_ips:  It is list of system IPs

        Returns:
            Returns list of tuple having system name and
            corresponding system IP.
        """
        system_ip_map = []
        if not system_names or not system_ips:
                print "List is empty!!! Please enter some data"
                return  system_ip_map

        system_no = min(len(system_names),len(system_ips))

        for x in range (0,system_no):
                system_ip_map += [(system_names[x],system_ips[x])]

        return system_ip_map

_list = raw_input("Enter system names seperated by coma : ")
system_names = _list.split(',')
_list = raw_input("Enter system IPs seperated by coma : ")
system_ips = _list.split(',')
print get_system_to_ip_map(system_names, system_ips)
