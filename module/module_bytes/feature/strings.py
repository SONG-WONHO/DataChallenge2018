import subprocess


def getLengthCnt(file_name):
    root_path = '../'

    # columns names
    col_cnt = ['stringLenCounts_' + str(i) for i in range(1, 100)] + [
        'stringLenCountsMore100',
        'stringLenCounts_0_10',
        'stringLenCounts_10_30',
        'stringLenCounts_30_60',
        'stringLenCounts_60_90',
        'stringLenCounts_90_inf',
        'stringLenCounts_0_100',
        'stringLenCounts_100_150',
        'stringLenCounts_150_250',
        'stringLenCounts_250_400',
        'stringLenCounts_400_600',
        'stringLenCounts_600_900',
        'stringLenCounts_900_1300',
        'stringLenCounts_1300_2000',
        'stringLenCounts_2000_3000',
        'stringLenCounts_3000_6000',
        'stringLenCounts_6000_15000',
        'stringLenCounts_15000_30000',
        'stringLenCounts_30000_60000',
        'stringLenCounts_60000_90000',
        'stringLenCounts_90000_150000',
        'stringLenCounts_150000_inf',
        'stringTotalLen']

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in col_cnt:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # get strings
    lines = subprocess.check_output("strings.exe -a -n 1 {}".format(file_path)).splitlines()[5:]
    lines = [v.decode('utf-8') for v in lines]

    for line in lines:

        # 특정 길이의 문자열이 몇 개 인지
        length = len(line)

        try:
            feature_list['stringLenCounts_' + str(length)] += 1
        except:
            feature_list['stringLenCountsMore100'] += 1

        if 0 <= length < 10:
            feature_list['stringLenCounts_0_10'] += 1
        elif 10 <= length < 30:
            feature_list['stringLenCounts_10_30'] += 1
        elif 30 <= length < 60:
            feature_list['stringLenCounts_30_60'] += 1
        elif 60 <= length < 90:
            feature_list['stringLenCounts_60_90'] += 1
        else:
            feature_list['stringLenCounts_90_inf'] += 1

    # 바이너리에 문자열이 몇 개 인지
    length = len(lines)

    if 0 <= length < 100:
        feature_list['stringLenCounts_0_100'] += 1
    elif 100 <= length < 150:
        feature_list['stringLenCounts_100_150'] += 1
    elif 150 <= length < 250:
        feature_list['stringLenCounts_150_250'] += 1
    elif 250 <= length < 400:
        feature_list['stringLenCounts_250_400'] += 1
    elif 400 <= length < 600:
        feature_list['stringLenCounts_400_600'] += 1
    elif 600 <= length < 900:
        feature_list['stringLenCounts_600_900'] += 1
    elif 900 <= length < 1300:
        feature_list['stringLenCounts_900_1300'] += 1
    elif 1300 <= length < 2000:
        feature_list['stringLenCounts_1300_2000'] += 1
    elif 2000 <= length < 3000:
        feature_list['stringLenCounts_2000_3000'] += 1
    elif 3000 <= length < 6000:
        feature_list['stringLenCounts_3000_6000'] += 1
    elif 6000 <= length < 15000:
        feature_list['stringLenCounts_6000_15000'] += 1
    elif 15000 <= length < 30000:
        feature_list['stringLenCounts_15000_30000'] += 1
    elif 30000 <= length < 60000:
        feature_list['stringLenCounts_30000_60000'] += 1
    elif 60000 <= length < 90000:
        feature_list['stringLenCounts_60000_90000'] += 1
    elif 90000 <= length < 150000:
        feature_list['stringLenCounts_90000_150000'] += 1
    else:
        feature_list['stringLenCounts_150000_inf'] += 1

    # Total Num of Strings
    feature_list['stringTotalLen'] = length

    temp_1 = ['stringLenCounts_3', 'stringLenCounts_6', 'stringLenCounts_4', 'stringLenCounts_2', 'stringLenCounts_0_10',
              'stringLenCounts_34', 'stringLenCounts_12', 'stringTotalLen', 'stringLenCounts_1', 'stringLenCounts_62',
              'stringLenCounts_5', 'stringLenCounts_30_60', 'stringLenCounts_25', 'stringLenCounts_10_30', 'stringLenCounts_9',
              'stringLenCounts_8', 'stringLenCounts_10', 'stringLenCounts_7', 'stringLenCounts_32', 'stringLenCounts_14',
              'stringLenCounts_21', 'stringLenCounts_50', 'stringLenCounts_11', 'stringLenCounts_26', 'stringLenCounts_13',
              'stringLenCounts_16', 'stringLenCounts_49', 'stringLenCounts_18', 'stringLenCounts_40', 'stringLenCounts_36',
              'stringLenCounts_19', 'stringLenCounts_23', 'stringLenCounts_17', 'stringLenCounts_55', 'stringLenCounts_27',
              'stringLenCounts_15', 'stringLenCounts_24', 'stringLenCounts_28', 'stringLenCounts_22', 'stringLenCounts_48',
              'stringLenCounts_60_90', 'stringLenCounts_29', 'stringLenCounts_39', 'stringLenCounts_20', 'stringLenCounts_41',
              'stringLenCounts_38', 'stringLenCounts_42', 'stringLenCounts_46', 'stringLenCounts_31', 'stringLenCounts_30',
              'stringLenCounts_90_inf', 'stringLenCountsMore100', 'stringLenCounts_33', 'stringLenCounts_35', 'stringLenCounts_53',
              'stringLenCounts_52', 'stringLenCounts_66', 'stringLenCounts_43', 'stringLenCounts_54', 'stringLenCounts_45',
              'stringLenCounts_61', 'stringLenCounts_73', 'stringLenCounts_71', 'stringLenCounts_64', 'stringLenCounts_74',
              'stringLenCounts_37', 'stringLenCounts_47', 'stringLenCounts_44', 'stringLenCounts_63', 'stringLenCounts_70',
              'stringLenCounts_51', 'stringLenCounts_67', 'stringLenCounts_76', 'stringLenCounts_68', 'stringLenCounts_60',
              'stringLenCounts_69', 'stringLenCounts_58', 'stringLenCounts_59', 'stringLenCounts_95', 'stringLenCounts_57',
              'stringLenCounts_77', 'stringLenCounts_90', 'stringLenCounts_56', 'stringLenCounts_65', 'stringLenCounts_72',
              'stringLenCounts_84', 'stringLenCounts_94', 'stringLenCounts_75', 'stringLenCounts_79', 'stringLenCounts_81']

    temp_2 = {'hash': file_name}

    for v in temp_1:
        temp_2[v] = feature_list[v]

    return temp_2


def getSymbol(file_name):
    root_path = '../'

    # column names
    col_sym = ['!', '?', '=', '+', '-', '*', '%', '[', ']', '{', '}', '(', ')', '@', '#', "'", '"', ';', ':', '.', ',']

    # make feature list (dict format)
    feature_list = {'hash': file_name}
    for v in col_sym:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # get strings
    lines = subprocess.check_output("strings.exe -a -n 1 {}".format(file_path)).splitlines()[5:]
    lines = [v.decode('utf-8') for v in lines]

    for line in lines:

        # symbol
        for sym in col_sym:
            feature_list[sym] += line.count(sym)

    return feature_list


def getMisc(file_name):
    root_path = '../'

    # column names
    col_misc = ['jz', 'malloc', 'kernel', 'DLL', 'dd', 'dw', 'free', 'lea', 'dll', 'public', 'alloc', '.exe',
                'security', 'user', 'db', 'init', '.dll', 'microsoft', 'windows', '__dllonexit', 'Virtual',
                'code', 'exe', 'loc_', 'global', 'Software', 'rep', 'xml', 'handler', 'strlen', 'gdi', 'memcpy',
                'proc', 'move', 'format', 'error', 'reg', 'load', 'arg', 'cmp', 'heap', 'file', 'add', 'fmode',
                'esi', 'CurrentVersion', 'int', 'failed', 'loc', 'tls', 'config', 'inc', 'word', 'std', 'unk',
                'environment', 'switch', 'resource', 'icm', 'DATA', 'Offset', 'src', 'sub', 'esp', 'call', 'var',
                'close', 'calloc', 'dec', 'struct', 'thread', 'virtual', 'rva', 'BOOL', 'create', 'off', 'char',
                'system', 'ptr', 'byte']

    # make feature list (dict format)
    feature_list = {'hash': file_name}
    for v in col_misc:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # get strings
    lines = subprocess.check_output("strings.exe -a -n 1 {}".format(file_path)).splitlines()[5:]
    lines = [v.decode('utf-8') for v in lines]

    for line in lines:

        # misc
        for misc in col_misc:
            if line.find(misc) != -1:
                feature_list[misc] = 1

    return feature_list
