###########################
### midi_csv_texthandle ###
###########################
"""This custom processing script (1) tokenizes pre-cleaned midi_csv and then (2) maps
csv tokens to ASCII characters,
"""

import itertools
import string
import sys
import tokenize

_ASCII_PRINTABLES_LIST = string.printable
_ASCII_CHARS_SET = set(''.join(map(str, [_ASCII_PRINTABLES_LIST[i] for i in range(88)])))

""
Note_on ffewf
Note_offe fesfef
Note_on jojbjtob
Note_off fefsifs
""

""
a $ % 3 bewigf6343 %^%&$e e3rhb 
""

""
fekjsf e^&%&^%hhgfrw@ hdeuinded 
""





