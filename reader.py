########################
### TEXT FILE READER ###
########################

# Copies all filenames for all text files in the directory.
# Preps all filenames for reading.
import glob
all_filenames, string_queue = glob.glob('*.txt'), []

# Reads the text files and returns stripped strings of theeir contents.
def read_file(filename):
	"""takes in filename and returns string of 
	all characters with all spaces removed"""
	with open(filename, 'r') as myfile:
		data = myfile.read().replace('\n', '')
	return data

# Operation to read all text files in the directory
def read_all():
	"""all of the text files names in the variable
	'all_filenames' are read and placed in a list"""
	for filename in all_filenames:
		string_queue.add(read_file(filename))
	return string_queue

# Stores all prepared strings in one list 
ready_strings = read_all()
