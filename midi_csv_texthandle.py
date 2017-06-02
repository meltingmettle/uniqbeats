###########################
### midi_csv_texthandle ###
###########################
"""This custom processing script (1) tokenizes pre-cleaned midi_csv and then (2) maps
csv tokens to numbers where middle C taken to be 0 and bass is negative, treble is positive.
"""
import string
import reader

cleaned = reader.run()

def split_token(token):
	atoms = token.split(", ")
	return atoms

def analyze_token(token_atoms):
	cur = token_atoms[2][6] 
	if cur == 'n':
		token_atoms[2] = 1
	elif cur == 'f':
		token_atoms[2] = 0
	else:
		raise ValueError("Error: non-Note token element")
	return token_atoms

def analyze_all(comp_list):
	data_set = []
	for token_list in comp_list:
		ref = []
		for token in token_list:
			token = split_token(token)
			ref.append(analyze_token(token))
		data_set.append(ref)
	return data_set

def run():
	return analyze_all(cleaned)