import json


def get_func_cnt(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/function.json"
    try:
        func = json.loads(open(file_path).read())

        feature_list = {'hash': file_name,
                        'FunctionCnt': len(func['function_all']),
                        'FunctionLibCnt': len(func['function_lib']),
                        'FunctionNoRetCnt': len(func['function_noret']),
                        'FunctionStatic': len(func['function_static']),
                        'FunctionThunk': len(func['function_thunk']),
                        'FunctionHidden': len(func['function_hidden'])}

    except:
        feature_list = {'hash': file_name}

    return feature_list
