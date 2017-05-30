###########################
### midi_csv_texthandle ###
###########################
"""This custom processing script (1) cleans midi_csv, (2) tokenizes midi_csv, and then (3) maps
csv tokens to ASCII characters,
"""

import itertools
import string
import sys
import tokenize

_ASCII_PRINTABLES_LIST = string.printable
_ASCII_CHARS_SET = set(''.join(map(str, [_ASCII_PRINTABLES_LIST[i] for i in range(88)])))

print(_ASCII_PRINTABLES_LIST)
print(_ASCII_CHARS_SET)
print(len(_ASCII_CHARS_SET))

