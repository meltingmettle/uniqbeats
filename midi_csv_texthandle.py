###########################
### midi_csv_texthandle ###
###########################
"""This custom processing script (1) tokenizes pre-cleaned midi_csv and then (2) maps
csv tokens to numbers where middle C taken to be 0 and bass is negative, treble is positive.
"""

import itertools
import string
import sys
import tokenize

token_list = []
prim_data_set = []
trackl_data_set = []

def split_token(token):
	atoms = token.split(", ")
	return atoms

def clean_token(token_atoms):
	cur = token_atoms[2][5] 
	if cur == 'n':
		token_atoms[2] = 1
	elif cur == 'f':
		token_atoms[2] = 0
	else:
		raise ValueError("Error: non-Note token element")

for token in token_list:
	prim_data_set += clean_token(split_token(token))\