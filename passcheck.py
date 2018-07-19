from hashlib import sha1
# Possibly use filesplit from pypi to split files to more manageable sizes.
# Split files down and store elsewhere, then prep each file for multithreading. 
inpath = "" # Password file location
x = sha1(input("Password to look for: ").encode("utf-8"))
p = 0
pp = 0
with open(inpath) as infile:
    for line in infile:
        p += 1
        if x.hexdigest().upper() in line:
            print("Hash found: \n")
            print(line)
            break
        if p == 5000000:
            p = 0
            pp += 1
            print(5*pp,"m hashes checked.")
