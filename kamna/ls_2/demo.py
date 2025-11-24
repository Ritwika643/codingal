#Activity-1 Basic file operations

#write to a file
with open ("sample.txt", "w") as f :
    f.write("Hello, World!\nThis is coding")

#Read the file
with open ("sample.txt", "r") as f :
    content = f.read()
    print("Full Content:\n", content)

#Splint content into words and store in a list
words = content.split()
print("\nSplit words:", words)

#Close file (not needed when using 'with', it auto-closes)
import os
filename = "sample.txt"

#Check if file exists
if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist. Creating a new one.....")
    with open (filename, "w") as f :
        f.write("New file created.")

import os
filename = "sample.txt"
#Delete the file
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted", filename)
else:
    print("File not found to be deleted")

#Check again
if os.path.exists(filename):
    print("the file still exists")
else:
    print("the file does not found")

#Activity 4
with open("sample.txt", "w") as f:
    f.write("Hello, World!\nThis is coding")
with open("data.txt", "w") as f:
    f.write("Data file created.")

#Step-2. To remove duplicates from a file
def remove_duplicates(input_file, output_file): 
    with open(input_file, "r") as infile:
        lines = f.readlines()
# Remove duplicate lines(order preserved)
    unique_lines = list(dict.fromkeys(lines))
    
    with open(output_file, "w") as outfile:
     f.writelines(unique_lines)

# Remove duplicates from both files
remove_duplicates("sample.txt", "sample_clean.txt")
remove_duplicates("data.txt", "data_clean.txt")

#Step-3. To merge both cleaned files into one
files_to_merge = ["sample_clean.txt", "data_clean.txt"]
with open("merged_output.txt", "w") as outfile:
    for fname in files_to_merge:
        with open(fname, "r") as infile:
            outfile.write(infile.readlines())

#Final output confirmation
print("Duplicates removed and files merged into 'merged_output.txt'")
print("Clean files: 'sample_clean.txt' and 'data_clean.txt'")
print("Merged file: 'merged_output.txt'")