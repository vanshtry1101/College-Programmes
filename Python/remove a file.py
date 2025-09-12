import os
if os.path.exists("dharmik.txt"):
    os.remove("dharmik.txt")
else:
    print("The file does not exist")    