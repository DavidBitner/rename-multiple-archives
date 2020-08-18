import os

i = first = last = 0
path = os.chdir(input("Input the directory: "))
first_parameter = str(input("Input the first parameter to look for: "))
last_parameter = str(input("Input the second parameter to look for: "))
for file in os.listdir(path):
    for cont in file:
        if first_parameter in cont:
            first = i + 1
        if last_parameter in cont:
            last = i
        i += 1
    new_file_name = f"{file[first:last]}"
    if new_file_name not in "":
        try:
            os.rename(file, new_file_name)
        except FileExistsError:
            print(f"Error! {file} cannot be renamed to {new_file_name}, because the file already exists")
    i = last = first = 0
