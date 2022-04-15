import os

path = os.chdir(input("Input the directory: "))
for file in os.listdir(path):
    new_file_name = f"@{file}"
    if new_file_name not in "":
        try:
            os.rename(file, new_file_name)
        except FileExistsError:
            print(f"Error! {file} cannot be renamed to {new_file_name}, because the file already exists")
    i = last = first = 0
