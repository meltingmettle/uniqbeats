"""This custom processing script (1) cleans pre-cleaned midi_csv and then (2) converts
them into workable data structures.
"""

import reader
import string

cleaned = reader.run()

def split_token(token):
	"""Splits a token into it's parts andd stores 
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

def analyze_all(comp_list):
	"""Takes a list of token_lists and returns a new 
	list of token_list where each token_list contains
	analyzed versions of its respective tokens. """
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