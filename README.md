# EncryptCSV
Python code to mask specific columns in CSV

There are two .py file in repository,
1. EncryptCSV.py - this script is to mask specific columns in the provided input file(input.csv) and write to the output file(output.csv)
   a. modify the headers are required for your input file, line 18
       for user, phonenumber, password in csv_input: 
   b. encrypt the required columns, line 19
        csv_output.writerow([user, hash(phonenumber), hash(password)])
   c. if required modify the script to desired masking algorithm, line 7
            return hashlib.sha256(text.encode('utf-8')).hexdigest()
3. CreateBigFile.py. this script is to create a csv file with infite loop ****please be mindfil to interupt the script once the required size is reached by cntrl+c as there is exit condition to the script and it requires close monioring to exit. it is a dirty script to just create a quick file of big size
