from os import system, walk

files_list = []

for (parent, folders, files) in walk(".") :
    for j in files :
        if j.endswith(".h") or j.endswith(".c") :
            strda = str(parent + '\\' + j)
            files_list.append(strda)

args = " ".join(files_list)

print(f"Compile GCC for PROJECT to main.exe")
"""
system(f"gcc -x c {args}-o main.exe && main.exe")
print("\n")
"""