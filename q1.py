# CS421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Assignment 1
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully. If you want to use external packages (not specified in
# the assignment) then you need prior approval from course staff.
# This part of the assignment will be graded automatically using Gradescope.
# =========================================================================================================

import re



# Sample function which returns a regex to represent a set of strings containing only the capital letters
# Note that it returns a raw python string (preceded by r) which saves us from the backslash plague
# More details here https://docs.python.org/3.7/howto/regex.html#the-backslash-plague
def capital_letters():
	# ^ signifies the start of string and $ signifies end of string
	# [A-Z] indicates all capital letters
	# [A-Z]+ indicates one or more capital letters
    return r"^[A-Z]+$"


# Q1(a): the set of strings that contain no letters or digits
# Returns: regex as a valid python string
def letters_digits():   #empty string problem
	# [YOUR CODE HERE]

	#not [0-9][A-Z][a-z]

	return r"^[^0-9a-zA-Z]*$"


# Q1(b): the set of string 
def upper_lower():
	# [YOUR CODE HERE]
	return r"^[A-Z]+$|^[a-z]+$"


# Q1(c): the set of all plural English words, under the simplifying assumption that all English plurals end in s or es
# Return: regex as a valid python string
def plural_words():
	# [YOUR CODE HERE]
	return r"^([a-zA-Z])+(s|es)$"


# Q1(d): the set of all strings from the alphabet a, b such that each a is never preceded or followed by another a
# Return: regex as a valid python string
def alpha_ab():
	# [YOUR CODE HERE]
	return r"^((a|b)(ba|b)*)$"


# Q1(e): the set of all strings that start with a word and that end with one or more digits
# Return: regex as a valid python string
def word_digits():   #TODO
	return r"^(\s*[a-zA-Z]*[0-9]+)+$"


# Q1(f): the set of all strings that have the exact words 'corona' and 'virus' in them
# Return: regex as a valid python string
def coronavirus():	#TODO	
	# [YOUR CODE HERE]
	# corona123virus corona virus
	return r"^(.*\bcorona.*\bvirus.*)|(.*\bvirus.*\bcorona.*)$"


# Q1(g): the set of all strings that have exactly one digit in them
# Return: regex as a valid python string
def one_digit(): 
	# [YOUR CODE HERE]
	return r"^[0-9]$"


# Q1(h): the set of all strings that have a slash (/) in them
# Return: regex as a valid python string
def slash():
	# [YOUR CODE HERE]
	return r"^.*/.*$"


# Q1(i): the set of all strings that have no whitespace in them
# Return: regex as a valid python string
def whitespace():
	# [YOUR CODE HERE]
	return r"^[\S]*$"


# Q1(j):  the set of all English proper nouns, under the simplifying assumption that all English proper nouns have the first letter of each word capitalized
# Return: regex as a valid python string
def proper_nouns():		#TODO
	# [YOUR CODE HERE]
	return r"^([A-Z][a-zA-Z]*\s*)+$"
	#return r"^([A-Z][a-zA-Z]*)(\s[A-Z][a-zA-Z]*\s*)*$"



# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 q1.py
# It should produce the following output:
# 		$ python3 q1.py 
# 		Match: HELLOWORLD
# 		No Match: HELLO WORLD

def main():


	# Get the regex from function
	regex = word_digits()

	# Compile the regex
	p = re.compile(regex)

	# Let us test our regex with a valid string
	test = 'abaa1'
	match = p.match(test)	
	if match is None:
		print('No Match: {0}'.format(test))
	else:
		print('Match: {0}'.format(test))
	
	# Let us test our regex with an invalid string.
	# Why is it invalid?
	test = 'babbbb'
	match = p.match(test)
	if match is None:
		print('No Match: {0}'.format(test))
	else:
		print('Match: {0}'.format(test))



	"""
	# Get the regex from function
	regex = capital_letters()

	# Compile the regex
	p = re.compile(regex)

	# Let us test our regex with a valid string
	test = 'HELLOWORLD'
	match = p.match(test)
	if match is None:
		print('No Match: {0}'.format(test))
	else:
		print('Match: {0}'.format(test))
	
	# Let us test our regex with an invalid string.
	# Why is it invalid?
	test = 'HELLO WORLD'
	match = p.match(test)
	if match is None:
		print('No Match: {0}'.format(test))
	else:
		print('Match: {0}'.format(test))

	"""



################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
