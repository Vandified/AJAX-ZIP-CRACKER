import zipfile
import os
import sys

print("\033[91\nm========Zip File Password Crackee========\n")
print("\033[92m     / \        | |    / \    \ \/ /            ")
print("    / _ \    _  | |   / _ \    \  /             ")
print("   / ___ \  | |_| |  / ___ \   /  \             ")
print("  /_/   \_\  \___/  /_/   \_\ /_/\_\ \n")
print("\033[91mAuthor: A J A X(vandi_fied)\nI am Not Responsible For Use This Program\nUse This At Your Own Risk")
print("\033[0m")

count = 1

zip_filename = input("Enter Zip File Name You Want To Crack: ")
pass_filename = input("Enter PasswordList File Name: ")

# Check if the file exists in the current directory and is a zip file
if not (os.path.isfile(zip_filename) and zip_filename.endswith('.zip')):
	print(f"\033[91m{zip_filename} doesn't exists in the current directory.")
	sys.exit()
	
if not os.path.isfile(pass_filename):
	print(f"\033[91m{pass_filename} doesn't exists in the current directory.")
	sys.exit()
	
# Open and read the text file
with open(pass_filename, 'r') as file:
    # Read all lines, strip newline characters, and store them in a list
    lines = [line.strip() for line in file.readlines()]

# Create a dictionary to count occurrences
name_count = {}

# Count occurrences of each name
for name in lines:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

# Check if any name appears more than once
duplicates = {name: count for name, count in name_count.items() if count > 1}

# Output the result
if duplicates:
    print("\033[91mThe following password appear more than once:")
    for name, count in duplicates.items():
        print(f"{name}: {count} times")
        sys.exit()
else:
    print("No passwords appear more than once.")

with open(pass_filename,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(zip_filename,'r') as zf:
            	
                zf.extractall(pwd=password)

                # data = zf.namelist()[0]
                data = zf.namelist()
                # for file_name in data:
                    # print(f" {file_name},")

                # data_size = zf.getinfo(data).file_size
                data_size = sum(zf.getinfo(file_name).file_size for file_name in data)

                print('''\033[92m--------PASSWORD CRACKED SUCCESSFULLY--------\n\n[+] Password found!\n[Line: %s] Password: %s\nFiles: %s\nSize: %s\n''' 
                    % (count,password.decode('utf8'), data, data_size))
                break
        
        except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as e:
            # If extraction fails (incorrect password), continue to the next one
            number = count
            print('[%s] [-] Trying... - %s' % (number, password.decode('utf8')),'[-] failed')
            count += 1
            pass

        except Exception as e:
            print(f"\033[91mError: {e}")
    