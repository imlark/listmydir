import os
import sys
import argparse

def get_filepaths(directory):

    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
	# skip directors

    return file_paths  # Self-explanatory.

def processArgs(argv):
	# reference url : http://stackoverflow.com/questions/18335687/python-using-argparse-argumentparser-method	
	parser = argparse.ArgumentParser(description='List my dirs.')
	parser.add_argument("indir", help="input directory name")
	parser.add_argument("outdir", help="output directory name")

	# parser.print_help()
	args = parser.parse_args()

def main(argv):
	# Agument
	processArgs(argv)

	# srcDir 
	full_file_paths = get_filepaths("/Users/lark/Documents/Work/Workspace/simpleapp")
	# print full_file_paths


if __name__ == "__main__":
	main(sys.argv[1:])
