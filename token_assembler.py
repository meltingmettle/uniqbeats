"""This text converter and writer takes outputted data structs 
and then writes them into standard midi_csv text files.
"""

# import brain0
import reader
import token_analyzer
import string

##########################################
# Delete and replace with pipeline from AI
workable_data = token_analyzer.run()
##########################################

def make_strings(token_atom_list):
	"""Converts all atoms in each list of atoms
	into strings for later use in writer. """
	for i in range(len(token_atom_list)):
		token_atom_list[i] = str(token_atom_list[i])
	return token_atom_list

def notify(token_atom_list):
	"""Converts the numeric placemarker for the 
	Note back into its base midi_csv format. """
	if token_atom_list[2] == "1":
		token_atom_list[2] = "Note_on_c"
	elif token_atom_list[2] == "0":
		token_atom_list[2] = "Note_off_c"
	else:
		raise ValueError("Error: non-Note token element")
	return token_atom_list

def assemble_token(token_atom_list):
	"""Takes a single list of stringified token atoms
	and then joins them into a single token. """
	new_token = ", ".join(token_atom_list)
	return new_token

def assemble_all(data_set):
	"""Takes a data_set consisting of lists of 
	atomized tokens, stringifies/notifies them, and
	then assembles them. """
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