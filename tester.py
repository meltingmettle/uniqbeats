import reader
import token_analyzer
import token_assembler
import writer 
import glob

emp = []
tru = []

test_input = reader.clean_metadata(reader.tokenize(reader.read_file('../uniqbeats/training_data/magnificat.txt')))

test_output = reader.tokenize(reader.read_file('../uniqbeats/output/zIvIFwVXQl.txt'))

print(test_input)
print(test_output)

print(test_input == test_output)