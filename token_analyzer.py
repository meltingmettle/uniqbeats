"""This custom processing script (1) cleans pre-cleaned midi_csv and then (2) converts
them into workable data structures.
"""

import reader
import string

cleaned = reader.run()

def split_token(token):
	"""Splits a token into atomic parts and stores 
	them in a list. """
	atoms = token.split(", ")
	return atoms

def analyze_token(token_atoms):
	"""Changes the Note syntax into numeric values,
	namely 0's and 1's.  """
	cur = token_atoms[2][6] 
	if cur == 'n':
		token_atoms[2] = 1
	elif cur == 'f':
		token_atoms[2] = 0
	else:
		raise ValueError("Error: non-Note token element")
	return token_atoms

def make_ints(analyzed_token_atoms):
	"""Makes the value of each token's atoms integers 
	for data processing. """
	for i in range(len(analyzed_token_atoms)):
		analyzed_token_atoms[i] = int(analyzed_token_atoms[i])
	return analyzed_token_atoms

def convert_all(comp_list):
	"""Takes a list of token_lists and returns a new 
	data_set consisting of lists of atomized and 
	analyzed tokens for each composition in comp_list. """
	data_set = []
	for token_list in comp_list:
		ref = []
		for token in token_list:
			ref.append(make_ints(analyze_token(split_token(token))))
		data_set.append(ref)
	return data_set

def run():
	return convert_all(cleaned)