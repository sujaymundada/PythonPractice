import os

directory_ = "/Users/sujay/Python"
filename_ = "concat.py"


with open(os.path.join(directory_,filename_)) as f:
    print(f.read())
