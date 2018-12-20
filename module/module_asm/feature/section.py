import numpy as np
import pandas as pd
import json


def get_section_name_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/section.csv"

    colnames = {'.idata': 0, '.data': 0, '.text': 0, '.rdata': 0,
                '.tls': 0, '.ndata': 0, 'seg000': 0, '.strings': 0,
                '.bss': 0, 'DATA': 0, 'CODE': 0, 'BSS': 0,
                'UPX0': 0, 'UPX1': 0, '.rsrc': 0, 'HEADER': 0,
                '.itext': 0, '.gfids': 0, 'UPX2': 0, '.CRT': 0,
                '.code': 0, '.': 0, '.reloc': 0, '.didat': 0,
                '.aspack': 0, '.adata': 0, '.didata': 0, '.bak': 0,
                '.vmp1': 0, '.brdata': 0, '.idata__': 0, '.vmp0': 0,
                'petite': 0, 'rdata': 0, 'GAP': 0, '.DATA': 0,
                'seg001': 0, 'section_etc': 0,
                'hash': file_name}

    try:
        section = pd.read_csv(file_path)

        for v in section.name.values:
            try:
                colnames[v] += 1
            except:
                colnames['section_etc'] += 1

    except:
        pass

    return colnames


def get_exec_section_name_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/section.csv"

    colnames = {'.text': 0, '.idata': 0, 'UPX0': 0, 'CODE': 0,
                'UPX1': 0, '.itext': 0, '.rsrc': 0, '.code': 0,
                '.data': 0, '.': 0, '.bak': 0, '.reloc': 0,
                '.vmp1': 0, '.seg000': 0, '.brdata': 0, '.vmp0': 0,
                'INIT': 0, 'section_etc': 0}

    try:
        section = pd.read_csv(file_path)

        for v in section[section.x == 1].name.values:
            try:
                colnames[v] += 1
            except:
                colnames['section_etc'] += 1

    except:
        pass

    # 모든 섹션 이름 빈도와 중복을 피하기 위함
    temp = {'hash': file_name}

    for name in colnames:
        temp[name + '_exe'] = colnames[name]

    return temp


def get_section_entropy(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # pe path
    file_path = root_path + dir_name + "/pe.json"

    try:
        pe = json.loads(open(file_path).read())

        # deafult feature list
        feature_list = {}

        entropies = []

        for v in pe['Sections'].keys():
            entropies.append(pe['Sections'][v]['Entropy'])

        # max, average, more than 7 cnt
        feature_list['EntropyMax'] = np.max(entropies)
        feature_list['EntropyMean'] = np.mean(entropies)
        feature_list['EntropyStd'] = np.std(entropies)
        feature_list['EntropyMoreThan7Cnt'] = np.sum([(v > 7) * 1 for v in entropies])

    except:
        feature_list = {}

    feature_list['hash'] = file_name

    return feature_list


def get_section_info(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # file path
    file_path = root_path + dir_name + "/section.csv"

    # deafult feature list
    feature_list = {'hash': file_name}

    try:
        section = pd.read_csv(file_path)

        feature_list = getSectionCnt(section, feature_list)
        feature_list = getSectionCntWithPermission(section, feature_list)
        feature_list = getSectionSize(section, feature_list)

    except:
        pass

    return feature_list


# 섹션 개수
def getSectionCnt(section, feature_list):
    feature_list['SectionCnt'] = len(section)
    return feature_list


# 권한 있는 섹션 개수 - 실행, 쓰기
def getSectionCntWithPermission(section, feature_list):
    feature_list['SectionExecutableCnt'] = section['x'].sum()
    feature_list['SectionWriteCnt'] = section['w'].sum()
    return feature_list


# 섹션 사이즈 - 모든 섹션과 실행권한이 있는 섹션
def getSectionSize(section, feature_list):

    #섹션의 합
    feature_list['SectionSizeSum'] = section['size'].sum()

    #실행권한이 있는 섹션의 사이즈 평균, 최대, 최소
    # 평균
    feature_list['SectionExecutionSizeMean'] = section[section.x == 1]['size'].mean()
    # 최대
    feature_list['SectionExecutionSizeMax'] = section[section.x == 1]['size'].max()
    # 최소
    feature_list['SectionExecutionSizeMin'] = section[section.x == 1]['size'].min()

    # 섹션 사이즈 - 모든 섹션 평균, 최대, 최소
    # 평균
    feature_list['SectionSizeMean'] = section['size'].mean()
    # 최대
    feature_list['SectionSizeMax'] = section['size'].max()
    # 최소
    feature_list['SectionSizeMin'] = section['size'].min()

    return feature_list

