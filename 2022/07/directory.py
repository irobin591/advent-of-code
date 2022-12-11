class Directory:
    def __init__(self, dir_name='/', parent=None, layer=0):
        self.dirs = {}
        self.files = {}
        self.dir_name = dir_name
        self.parent = parent
        self.layer = 0

    def add_dir(self, dir_name):
        self.dirs[dir_name] = Directory(dir_name, self, self.layer+1)
        return self.dirs[dir_name]
    
    def add_file(self, file_name, file_size):
        self.files[file_name] = file_size

    def total_size(self):
        return sum(self.files.values()) + sum(sub_dir.total_size() for sub_dir in self.dirs.values())

    def chdir(self, dir_name):
        if dir_name == '..':
            return self.parent
        return self.dirs[dir_name]

    def get_directories(self):
        for sub_dir in self.dirs:
            yield sub_dir
