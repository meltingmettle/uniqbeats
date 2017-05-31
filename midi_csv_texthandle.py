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