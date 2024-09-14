# AJAX-ZIP-CRACKER

AJAX-ZIP-CRACKER is a Python script designed to crack passwords for encrypted ZIP files using a brute-force approach with a list of potential passwords. This script attempts to extract files from a ZIP archive using each password from a provided list until it finds the correct one.

## Features

- **Password Cracking**: Attempts to open a ZIP file with passwords from a specified list.
- **Duplicate Password Detection**: Identifies and notifies if any passwords in the list appear more than once.
- **Detailed Output**: Provides feedback on the progress and results of the password cracking attempt.

## Requirements

- Python 3.x
- ZIP file to crack
- Password list file (text file with one password per line)

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Vandified/AJAX-ZIP-CRACKER.git
   cd AJAX-ZIP-CRACKER
   ```

2. **Prepare Your Files**
   - Ensure you have the ZIP file you want to crack.
   - Prepare a text file with a list of passwords (one per line).

3. **Run the Script**
   ```bash
   python3 cracker.py
   ```
   - Enter the name of the ZIP file you want to crack.
   - Enter the name of the password list file.

4. **Review Results**

   - The script will output the results, including whether the password was successfully found and details about the extracted files.

## Notes

This script is intended for educational purposes and ethical use only.
The author is not responsible for any misuse of this program. Use at your own risk.

## Author
### A J A X (vandi_fied)

**For more information, contact me at [DISCORD](https://discord.com/users/732138466749579324)**
