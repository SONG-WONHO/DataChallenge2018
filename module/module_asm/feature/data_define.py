def get_dd_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/data_define.txt"

    colnames = ['dd', 'dw', 'db']

    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0
    try:
        dd_list = open(file_path, 'r').read().split(',')

        for register in dd_list:
            try:
                feature_list[register] += 1

            except:
                pass

    except:
        pass

    return feature_list
