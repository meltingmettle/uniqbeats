#################
### reader.py ###
#################
""" This reader (1) takes input textfiles containing midi_csv, (2) cleans up the strings, 
and then (3) spits out an edited text file for later usage. Modified for pipelined streaming.
"""

# Copies all filenames for all text files in the directory.
import glob
chars, all_filenames, string_queue, cleaned = set('HSTCENIP'), glob.glob('*.txt'), [], []

def read_file(filename):
	"""Takes in filename and returns string of 
	all text content."""
	with open(filename, 'r') as myfile:
		data = myfile.read()
	return data

def tokenize(data):
	return data.split('\n')

def first_char(string):
	i = 0
	while string[i] not in chars:
		i += 1
	return string[i]

def clean_metadata(token_list):
	"""Assumption: header is included in the midi_csv file used.
	Future: incorporate this to generalize for all possible files."""
	return [token for token in token_list if first_char(token) == 'N']

# Operation to read all text files in the directory and then clean the resulting strings
for filename in all_filenames:
	string_queue.append(tokenize(read_file(filename)))
for i in range(len(string_queue)):
	cleaned.append(clean_metadata(string_queue[i]))