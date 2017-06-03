"""This custom, processing script takes composition lists consisting of  midi_csv tokens and writes each token (as a string) into a text file for each composition, creating a pseudo-random name for each file.
"""

import random
import os
import string

chars = list(string.ascii_letters)
save_path = '../uniqbeats/output'

def combine_strings(string_list):
	"""Takes a list of strings and combines them 
	into a single string. """
	return '\n'.join(string_list)

def write_file(string):
	"""Writes a string into a given file whose
	filename consists of randomly-generated string of
	ASCII uppercase/lowercase chars and digits. """
	filename = ''.join(random.choice(chars) for _ in range(10))
	with open(os.path.join(save_path, filename + ".txt"), "w") as file:
		file.write(string)
	return filename

def write_all(comp_list):
	"""Writes all of the string_lists in a given
	comp_list to each comp_list's respective file. """
	for string_list in comp_list:
		filename = write_file(combine_strings(string_list))
		print(filename)