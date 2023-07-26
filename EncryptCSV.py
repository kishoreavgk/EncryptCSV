#Script to mask the specific fields in CSV

import hashlib
import csv

def hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_file(input_file_name, output_file_name): 
    hash_lookup = {} 

    with open(input_file_name, newline='') as f_input, open(output_file_name, 'w', newline='') as f_output: 
        csv_input = csv.reader(f_input)
        csv_output = csv.writer(f_output) 
        csv_output.writerow(next(csv_input))    # Copy the header row to the output

        for user, phonenumber, password in csv_input: 
            csv_output.writerow([user, hash(phonenumber), hash(password)]) 

hash_file('input.csv', 'output.csv')