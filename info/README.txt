~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~ UniqBeats: Gradient-descent Intelligence ~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~ creating music for a 21st-century world  ~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(1) Text Processing

### Description: The musical content of MIDI files can be encapsulated in their respective CSV.
CSV format can be converted into simpler strings of symbols. Symbolic abstraction: a given intelligence
doesn't need to know what the concept of 'music' is, nor does it have to be able to appreciate the beauty 
of good music; it just needs to see and learn the symbolic patterns behind the masterpieces in order 
to be able to generate its own symbols, which we then reinterpret as CSV and ultimately as MIDI files.

### Components:

  - CSV Cleaner
  # Reduces CSV files to their musical content (notes, pitches, rhythm, etc.)
  # Cleanup of any extraneous musical content
  
  - Text File Reader
  # Organizes and then reads the text files
  # Converts text files into strings 
  # Puts read strings into queue for further processing
  
  - TBM (Tokenizer-Buffer-Mapper)
  # Tokenizer: splits up input text into tokens (individual notes)
  # Buffer: object that (i) puts tokens in a queue and (ii) keeps pointers to currently-used tokens and remaining tokens
  # Mapper: object that maps a given token to symbol using a built-in dictionary

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(2) Gradient-descent Intelligence

### Description: <SPECIFICS ARE CURRENTLY BEING HANDLED>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(3) Training Data Streaming

### Description: We want to be able to implement a continuously updated stream of select musical 
compositions that are readily converted to CSV and then into the feed-language that our AI will 
then be able to read. 

### ACCEPTABLE GENRES: Classical Music, Swing, Blues
### EX OF UNACCEPTABLE GENRES: Free-form Jazz, Folk/Cultural Music, <Anything with a pentatonic scale>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
