"""
PURPOSE OF FILE: 
  -To have the ability to extract certain attributes of a MIDI line (i.e. a timestamp, velocity, etc.)
  -Append a "distance_from_c" value to each MIDI line
  -Explore the use of TensorFlow and other libraries for analyzing data
"""


import token_analyzer

data = token_analyzer.run()
middleC = 60


def append_dist_from_c(midi_note):
	"""
	Adds a distance_from_c value to the end of a MIDI line
	"""
	note_val = midi_note[4]
	midi_note.append(note_val - middleC)

def create_dict(midi_note):
	"""
	Takes in a MIDI object in list form (i.e. [2,960,'Note_on_c',1,81,81]) and reformats to be a dictionary
	with keys corresponding to the names of each value to be more easily analyzed.
	(i.e. {'track':2, 'timestamp':960, 'action':'Note_on_c', 'channel':1, 'note':81, 'velocity':81, 'distance':21}) 
	"""
	converted = {}
	for i in range(len(midi_note)):
		if i == 0:
			converted['track'] = midi_note[i]
		elif i == 1:
			converted['timestamp'] = midi_note[i]
		elif i == 2:
			converted['action'] = midi_note[i]
		elif i == 3:
			converted['channel'] = midi_note[i]
		elif i == 4:
			converted['note'] = midi_note[i]
		elif i == 5:
			converted['velocity'] = midi_note[i]
		else:
			converted['distance'] = midi_note[i]
			
	return converted
			
	
def run_converter():
	revised_data = []
	
	for file in data:
		new_file = []
		for note in file:
			append_dist_from_c(note)
			new_file.append(create_dict(note))
		
		revised_data.append(new_file)
	
	return revised_data
	
	
print(run_converter())
	
#-------------------------------SEPARATE FUNCTION FOR DATA EXTRACTION----------------------------------
	
def extract_attr(file=0, *args):
	"""
	Takes in a string arguments(s) (i.e. "timestamp", "velocity", "note", etc) and returns a list of all those values
	from the specified MIDI file (default file is defined in case a file isn't specified in the function call.
	"""
	try:
		working_file = run_converter()[file]
	except IndexError:
		print("Specified file does not exist. Using last file in data")
		working_file = run_converter()[-1]
		
	extracted = []
	
	for note in working_file:
		for arg in args:
			extracted.append(note[arg])
	
	return extracted	
	
#print(extract_attr(4, 'timestamp'))