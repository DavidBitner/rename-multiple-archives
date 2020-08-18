import os

path = os.chdir(input("Input the directory: "))
i = first = last = 0

for file in os.listdir(path):
    for cont in file:
        if "(" not in cont:
            i += 1
        if "(" in cont:
            first = i + 1
        if ")" in cont:
            last = i
    new_file_name = f"{file[first:last]}"
    if new_file_name not in "":
        while True:
            try:
                os.rename(file, new_file_name)
            except FileExistsError:
                print(f"Error! {file} cannot be renamed to {new_file_name}, because the file already exists")
            finally:
                break
    i = last = first = 0
