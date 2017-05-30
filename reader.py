#################
### reader.py ###
#################
""" This reader takes an input textfile containing midi_csv, cleans up the strings, and then
spits out an edited text file for later usage. Modified for pipelined streaming.
"""

# Copies all filenames for all text files in the directory.
import glob
all_filenames, string_queue = glob.glob('*.txt'), []

def read_file(filename):
	""" Takes in filename and returns string of 
	all text content with spaces removed. """
	with open(filename, 'r') as myfile:
		data = myfile.read().replace('\n', '')
	return data

# Operation to read all text files in the directory
for filename in all_filenames:
	string_queue.append(read_file(filename))
