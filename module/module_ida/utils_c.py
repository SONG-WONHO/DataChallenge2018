def get_file_list(path_dir, ext):
    import os

    file_names = [f for f in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, f))]
    file_names = [x for x in file_names if x.find(ext) != -1]
    
    return file_names


def make_dir(file_names):
    import os
    import errno

    for fn in file_names:

        fn = fn.split(".")[0]

        try:
            if not (os.path.isdir('./result/' + fn)):
                os.makedirs(os.path.join('./result', fn))

        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory")
                raise