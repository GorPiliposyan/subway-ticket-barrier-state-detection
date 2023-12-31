# Python program to rename all file
# names in your directory
import os
import sys

args = sys.argv
code_file_name = args[0]
# directory = args[1]
while 1:
	directory = input("\n\nPlease input the path to the directory, where the files to be renamed are located:\n")
	print("\nYou have named the directory path as: ", directory, "\n")
	while 1:
		answer = input("Are you sure you want to rename files in that direcotry? [y]/n\n").lower()
		if answer in ["", "y", "n","yes","no"]:
			break
		else:
			print("Please provide a valid answer!")
	if answer in ["","y","yes"]:
		break

os.chdir(directory)
# print(os.getcwd())



# new_f_name = args[2]
new_f_name = input("\nPlease input the new file name:\n")




# try:
# 	new_f_ext = args[3]
# except:
# 	print("No file extension specified. Choosing .jpg as default file extension.")
# 	new_f_ext = "jpg"
new_f_ext = input("Please choose file extensions. Leave blank to keep the existing extensions.\n")
if new_f_ext == "":
	update_ext = False
else:
	update_ext = True





while 1:
	initial_id = int(input('\n\nPlease input the starting index value:\n'))
	if isinstance(initial_id, int):
		break
	print("\nThere is an issue with your input. The input for initial index should be an integer number.")


for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = new_f_name + "_" + str(initial_id + count)

	if update_ext:
		new_name = f'{f_name}.{new_f_ext}'.lower()
	else:
		new_name = f'{f_name}{f_ext}'.lower()
	os.rename(f, new_name)
