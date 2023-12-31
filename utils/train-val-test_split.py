# Python program to split the dataset into
# training and validation datastes

import os
import numpy as np

np.random.seed(42)

train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1
acceptable_inputs = ["y", "n","yes","no"]

while 1:
	directory = input("\n\nPlease input the path to the working directory\n")
	print("\nYou have named the directory path as:\n", directory, "\n")
	while 1:
		answer = input("Are you sure you want use this direcotry? y/n\n").lower()
		if answer in acceptable_inputs:
			break
		else:
			print("Please provide a valid answer! Acceptable inputs include: {}".format(acceptable_inputs))
	if answer in ["y","yes"]:
		break


# Find info about available files in the dataset.
os.chdir(directory)
# print(os.getcwd())
all_files = np.array(os.listdir(os.getcwd()))


# Shuffle the dataset indices
N = len(all_files)
idx = np.arange(N, dtype=int)
np.random.shuffle(idx)
train_idx = idx[:int(N*train_ratio)]
val_idx = idx[int(N*train_ratio):int(N*(train_ratio+val_ratio))]
test_idx = idx[int(N*(train_ratio+val_ratio)):]


# Do the split, i.e. separate training and validation groups



train_files = all_files[train_idx]
val_files = all_files[val_idx]
test_files = all_files[test_idx]


print("Training file indices in the directory:\n", train_idx)
print("Training file names:\n", train_files)
print()
print("Validation file indices in the directory:\n", val_idx)
print("Validation file names:\n", val_files)
print()
print("Test file indices in the directory:\n", test_idx)
print("Test file names:\n", test_files)

# Move files to training and validation directories
current_dir = os.getcwd()

# For training
train_folder = os.path.join(current_dir, 'training')
if not os.path.exists(train_folder):
	os.makedirs(train_folder)
for file in train_files:
	os.rename(file, os.path.join(train_folder, file)) # os.path.basename(file)))


# For validation
val_folder = os.path.join(current_dir, 'validation')
if not os.path.exists(val_folder):
	os.makedirs(val_folder)
for file in val_files:
	os.rename(file, os.path.join(val_folder, file)) # os.path.basename(file)))

# For test
test_folder = os.path.join(current_dir, 'test')
if not os.path.exists(test_folder):
	os.makedirs(test_folder)
for file in test_files:
	os.rename(file, os.path.join(test_folder, file)) # os.path.basename(file)))


















