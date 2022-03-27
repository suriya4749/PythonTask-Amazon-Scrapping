__author__ = 'suriyakumar.s2'

import helper
import pdb
import re





#Prefixes the domain name in url
def prefix_url(url, prefix):
	if prefix not in url:
		return url.replace("&amp;", "&").replace('/',prefix, 1)
	return url

def prefix_string(url, prefix):
	if prefix not in url:
		return prefix + url
	return url
	
#Remove some characters from a string
def remove_char(targetString,stringRemove):
	return targetString.replace(stringRemove,"")



#Remove some characters from a string using re
def remove_char_re(targetString,stringRemove,stringReplace):
    return re.sub(stringRemove,stringReplace, targetString)

#Replace stringRemove with stringReplace
def replace_char(targetString,stringRemove,stringReplace):
	return targetString.replace(stringRemove,stringReplace)

# Checks if it contains url and sets containsUrl key				 
def check_url_status(input_string):
	return str(input_string is not None)
	
def remove_meta_char(target_string):
	#pdb.set_trace()
	target_string = helper.remove_meta_char(target_string)
	target_string = helper.remove_white_space(target_string)
	return target_string

def prefix_string(string,prefix):
	if prefix not in string:
		return prefix + string;
	return string		

def check_availability(string, search_string):
	if search_string in  string:
		return 'Y'
	return 'N'

def check_shipping_availability(string, search_string):
	if search_string in  string:
		return 'Known'
	return 'Unknown'
