def read_file(file_path):
    f = open(file_path, "r")
    return f.read().split()
