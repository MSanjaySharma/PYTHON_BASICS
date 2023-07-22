# Files

"""
A file operation takes place in the following order:
1. Open a file
2. Read or write (perform operation)
3. Close the file
"""

# 1. Open file
with open("v9.txt", "r+", encoding="utf-8") as f:
    f.write("line1\n")
    f.write("line3\n\n")
    f.write("line4\n")
    f.write("line5")
    print(f.readline())


"""
with open(<filename/path>, mode="", encoding="") as <variable_name>:
"""