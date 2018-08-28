import pip
import threading
from getpass import getpass
from hashlib import sha1
from multiprocessing import cpu_count

try:
    import psutil
except ImportError:
    print(" [ ! ] Package 'psutil' not found. This must be installed.")
    input(" [ ! ] Try running 'python -m pip install psutil' as administrator and try again...")
    exit()
try:
    from fsplit.filesplit import FileSplit
except ImportError:
    print(" [ ! ] Package 'filesplit' not found. This must be installed.")
    input(" [ ! ] Try running 'python -m pip install filesplit' as administrator and try again...")
    exit()

class Core:

    def __init__(self):
		self.thread_dispatcher()
		
	def file_breakdown(self):
		print(" [ i ] Determining split file size based on available memory...")
		filesize = psutil.virtual_memory().available / 2 # Only going to try and use 1/2 of available mem for any given action
		print(" [ i ] Splitting file to {:.0f} gb chunks.".format(round(filesize/(1024*1024*1024))))

    def thread_dispatcher(self):
		print(" [ i ] Setting number of threads based on logical cores...")
		threadcount = cpu_count()
		print(" [ i ] Set to", threadcount, "threads.")
		print(" [ i ] Creating and collecting threads...")
		fabric = []
		for i in range(num_threads):
            thread = threading.Thread(target=self.threaded_caller, args=(filename[i],passtarget))
            fabric.append(thread)
		print(" [ i ] {} threads created and collected.".format(len(fabric)))
		passtarget = sha1(getpass(" [ ? ] Password to look for: ").encode("utf-8"))

	def thread_caller(self, filename, passtarget)
		inpath = filename # Password file location
		p = 0
		pp = 0
		with open(inpath) as infile:
			for line in infile:
				p += 1
				if x.hexdigest().upper() in line:
					print("Hash found:")
					print(line)
					break
				if p == 5000000:
					p = 0
					pp += 1
					print(5*pp,"million hashes checked.")
