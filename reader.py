""" This reader (1) takes input textfiles containing midi_csv, (2) cleans up the strings, 
and then (3) spits out an edited text file for later usage. Modified for pipelined streaming.
"""

import glob
import string 

# Copies all filenames for all text files in the directory.
all_filenames = glob.glob('../uniqbeats/training_data/*.txt')
chars = set(string.ascii_uppercase) 
cleaned = []

def read_file(filename):
	"""Takes in filename and returns string of 
	all text content. """
	with open(filename, 'r') as myfile:
		data = myfile.read()
	return data

def tokenize(data):
	"""Splits string into lines and puts lines
	in a list. """
	return data.split('\n')

def first_char(string):
	"""Finds the first element in the string 
	that is in string.ascii_uppercase. """
	i = 0
	try: 
		while string[i] not in chars:
			i += 1
	except IndexError:
		return None
	return string[i]

def clean_metadata(tokenized_comp):
	"""Cleans extraneous info, leaving only the
	Note values in each tokenized composition. """
	return [token for token in tokenized_comp if first_char(token) == 'N']

# Operation to read all text files in the directory and then clean the resulting strings
def run():
	for filename in all_filenames:
		cleaned.append(clean_metadata(tokenize(read_file(filename))))
	return cleaned    