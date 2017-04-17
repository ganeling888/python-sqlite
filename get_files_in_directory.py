import os
# Go through every file in the directory that this script was executed in
for filename in os.listdir(os.getcwd()):
	# Print the filenames for each file
	print(filename)
