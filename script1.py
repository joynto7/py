import os
def current_directory():
    cwd=os.getcwd()
    print(cwd)
    current_directory

def file_path(filename):
    path = os.path.abspath(filename)
    print(path)
filename="sample.txt"
file_path(filename)