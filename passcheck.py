import getpass
import timeit
import hashlib

file_location = input(f"Location of file (ex: C:\\filename.txt): ")
found = False
with open(file_location) as file:
    beginning = 0
    firstline = file.readline()
    if len(firstline.split(":")[0]) > 32:
        hashlength = 40
        print("SHA-1 File detected.")
        inquery = hashlib.sha1(getpass.getpass(f"Password to look for: ").encode("utf-8")).hexdigest().upper()
    else:
        hashlength = 32
        print("NTLM File detected.")
        inquery = hashlib.new('md4',getpass.getpass(f"Password to look for: ").encode("utf-16le")).hexdigest().upper()
    if inquery in firstline: # Check the first line before starting.
        ending = 0
    else:
        ending = file.seek(0, 2)
    start_time = timeit.default_timer()
    while (ending - beginning > hashlength+3):
        temp_position = absolute_position = file.seek((ending + beginning)/2, 0)
        current_line = file.readline()
        while len(current_line.split(":")[0]) < hashlength: # Check if the first part of the split is too short (partial hash, or none at all)
            temp_position = temp_position - (hashlength - len(current_line.split(":")[0])) # Determine number of characters missing, and adjust position as necessary
            file.seek(temp_position)
            current_line = file.readline() # Re-assign the string, repeat process until aligned.
        file.seek(absolute_position) # Return to absolute positioning of the initial search
        if inquery in current_line:
            found = True
            break
        elif (inquery > current_line):
            beginning = file.tell()
        else:
            ending = file.tell()
    timed = (timeit.default_timer() - start_time)*1000

if found:
    print(f"Hashed version of password found. Number of times seen: " + current_line.split(":")[1])
else:
    print(f"Password not found in this file.")

print(f"Time spent searching: {timed:.5} milliseconds")
