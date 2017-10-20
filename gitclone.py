##
##	This script allows to execute git clone either normally
##	or giving two arguments "username" and "repository name"
##
 
import sys
import os
def main():
	long = len(sys.argv);
	if long == 2:
		os.system("git clone "+sys.argv[1]);
	elif long == 3:
		os.system("git clone https://github.com/"
			  +sys.argv[1]+"/"+sys.argv[2]+".git");
	return;

# main executes only if executing this file
if __name__== "__main__":
	main();
