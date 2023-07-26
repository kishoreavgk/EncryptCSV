#Script to mask the specific fields in CSV

import csv
import random
import string

def create_file(big_file_name): 
    with open(big_file_name, 'w+', newline='') as f_output: 
        csv_output = csv.writer(f_output)
        user=''.join(random.choices(string.ascii_letters + string.digits, k=10))
        phonenumber='0'.join(random.choices(string.ascii_letters + string.digits, k=9))
        password= ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        csv_output.writerow(['username','phonenumber','password'])  
        while 1 :
          csv_output.writerow([user, hash(phonenumber), hash(password)])

create_file('Bigfile.csv');