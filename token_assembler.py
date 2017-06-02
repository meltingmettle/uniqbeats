"""This text converter and writer takes outputted data structs and then writes them into standard midi_csv text files
"""

# import brain0
# import brain1
# ...
# import brainn

import reader
import midi_csv_texthandle
import string

cleaned = reader.run()
workable_data = midi_csv_texthandle.run()

def make_strings(token_atoms):
	for i in range(len(token_atoms)):
		token_atoms[i] = str(token_atoms[i])
	return token_atoms

def notify(token_atoms):
	if token_atoms[2] == "1":
		token_atoms[2] = "Note_on_c"
	elif token_atoms[2] == "0":
		token_atoms[2] = "Note_off_c"
	else:
		raise ValueError("Error: non-Note token element")
	return token_atoms

def assemble_token(token_atoms):
	new_token = ", ".join(token_atoms)
	return new_token

def assemble_all(data_set):
	"""Takes a data_set consisting of lists of 
	atomized tokens and then assembles all tokens 
	into their mid_csv formats. """
	comp_list = []
	for comp in data_set:
		ref = []
		for token_atom_list in comp:
			ref.append(assemble_token(notify(make_strings(token_atom_list))))
		comp_list.append(ref)
	return comp_list

def run():
	strings = assemble_all(workable_data)
	return strings

data_output = run()
print(data_output == cleaned)