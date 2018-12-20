import json


def get_dll_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/dll.json"

    colnames = {'kernel32': 0, 'user32': 0, 'advapi32': 0, 'gdi32': 0,
                'wininet': 0, 'comctl32': 0, 'shell32': 0, 'wsock32': 0,
                'oleaut32': 0, 'msvbvm50': 0, 'ole32': 0, 'shlwapi': 0,
                'ws2_32': 0, 'ntdll': 0, 'urlmon': 0, 'msvbvm60': 0,
                'hash': file_name}

    try:
        dll = json.loads(open(file_path).read())

        for dll_name in dll.keys():
            try:
                colnames[dll_name.lower()] += 1
            except:
                pass
    except:
        pass

    return colnames

