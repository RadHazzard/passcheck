import pip
from getpass import getpass
from hashlib import sha1
from multiprocessing import cpu_count

try:
    import psutil
except ImportError:
    print("[ ! ] Package 'psutil' not found. This must be installed.")
    input("[ ! ] Try running 'python -m pip install psutil' as administrator and try again...")
    exit()
try:
    from fsplit.filesplit import FileSplit
except ImportError:
    print("[ ! ] Package 'filesplit' not found. This must be installed.")
    input("[ ! ] Try running 'python -m pip install filesplit' as administrator and try again...")
    exit()

print("[ + ] Setting number of threads based on logical cores...")
threadcount = cpu_count()
print("[ + ] Set to", threadcount, "threads.")
print("[ + ] Determining split file size based on available memory...")
filesize = psutil.virtual_memory().available / 2 # Only going to try and use 1/2 of available mem for any given action
print("[ + ] Splitting file to {:.0f} gb chunks.".format(round(filesize/(1024*1024*1024))))

inpath = "pwned-passwords-ordered-by-count.txt" # Password file location
x = sha1(getpass("Password to look for: ").encode("utf-8"))
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
            print(5*pp,"million hashes checked.")
