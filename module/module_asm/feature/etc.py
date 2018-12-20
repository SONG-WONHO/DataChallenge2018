def get_etc_info(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    bin_size_path = root_path + dir_name + "/bin_size.txt"
    first_addr_path = root_path + dir_name + "/first_address.txt"
    num_of_lines_path = root_path + dir_name + "/number_of_lines.txt"

    try:
        bin_size = open(bin_size_path, 'r').readline()
        first_addr = open(first_addr_path, 'r').readline()
        num_of_lines = open(num_of_lines_path, 'r').readline()

        feature_list = {'hash': file_name, 'bin_size': bin_size, 'first_addr': first_addr, 'number_of_lines': num_of_lines}

    except:
        feature_list = {'hash': file_name}

    return feature_list
