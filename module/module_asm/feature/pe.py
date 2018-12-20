import json


def get_pe_info(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/pe.json"

    try:
        pe = json.loads(open(file_path).read())
    except:
        pe = {}

    pe['hash'] = file_name

    return pe
