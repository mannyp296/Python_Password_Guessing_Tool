Manuel Perez
CS 177 Homework 5
							Read me

My Tool: Crack.py

this tool attempts to crack a password given a user's shadow file.
Initially it performs a dictionary check  and then an incremental check
(brute force).

Initialize :::::
The program starts by opening the specified shadow file and taking the hashed
password string. The shadow file must be given on the command line when the
program is run:

./crack.py nameOfShadowFile

Only ONE string  of the shadow file is considered for the program, therefore
several separate shadow files must be run in succession if trying to crack different
passwords.

Dictionary check:

The program starts by asking the user to input a dictionary name to enter:

Enter dictionary to use:

Once the dictionary name is entered, the program will look for the dictionary
and use it as the lookup dictionary. A default dictionary is provided (500pass)
just in case. The function dictionaryFind() (line 36), initializes the dictionary
check.

Within the dictionary check, the program first goes throught a dictionary file and
checks the reverse of every word. After that, the program checks every possible
combination of the uppercase and lowercase characters for each word in the dictionary
file. This check by default includes checking every word in the dictionary file
as it is in the file. If this method does not work, the function checks for every
combination of two words from the dictionary. Alternatively, you can change the
second field on dictionaryFind() to combine every word from the dictionary with one
from a secondary dictionary. If the second field is an empty string ("") The program
will not perform this cheking method. If this method does not work the program
will proceed to brute-forcing the passwords.

Brute-force:
	
The last three parameters in dictionaryFind() (line 36) are for control options
for this fucntion. The 6th parameter provides 3 modes for the brute force attempt.
Modes:
0: No mode: The brute force portion is not active
1: Check for uppercase and lowercase alphabetic combinations only
2: check for alphanumeric combinations (Uppercase and lower case)
3: check for alphanmeroc/symbol combionationsb(95 characters)

The 7th parameter indicates the brutue-force starting word lenght to check. The 8th
parameter indicates the brute force maximum lenght to check. The mode, start,
and end parameters are by default set to 3(mode= 95 characters),0, and 8 respectively.
These fields can be changed to refine indivdual searches.

The program recognizes between DES and SHA-512 and runs all the mentioned strategies
the same.

Note:This program was made for learning purposes. The speed of the program is not optimized.