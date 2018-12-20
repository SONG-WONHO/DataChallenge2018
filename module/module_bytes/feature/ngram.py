import numpy as np


def get1gram(file_name):
    root_path = '../'
    n = 1

    # column names
    colnames = ['245', '173', '32', '134', '204', '231', '255', '113', '155', '48',
                '154', '222', '174', '175', '16', '117', '139', '167', '130', '59',
                '253', '116', '237', '64', '239', '149', '3', '106', '251', '6', '0',
                '15', '254', '153', '105', '157', '36', '162', '146', '166', '12', '133',
                '158', '131', '137', '77', '143', '233', '227', '4', '170', '5', '193',
                '250', '151', '86', '195', '1', '49', '196', '199', '171', '81', '89',
                '194', '85', '115', '123', '75', '110', '218', '20', '21', '198', '192',
                '93', '63', '226', '67', '159']

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    for i in range(len(file_bytes) - (n - 1)):

        # ex) if 3 gram, seq is '13.15.255'
        seq = ".".join(([str(v) for v in file_bytes[i:i + n]]))

        try:
            feature_list[seq] += 1
        except:
            pass

    return feature_list


def get2gram(file_name):
    root_path = '../'
    n = 2

    # column names
    colnames = ['134.247', '134.72', '85.4', '42.134', '3.85', '66.115', '48.130', '72.134', '33.11', '6.3', '85.29',
                '73.99', '48.13', '11.48', '46.68', '58.47', '121.65', '46.99', '247.13', '9.42', '112.58', '97.69',
                '13.1', '48.9', '195.195', '128.14', '86.77', '43.6', '48.129', '13.6', '130.1', '251.160', '6.1',
                '113.181', '1.11', '192.192', '27.64', '255.252', '22.114', '255.40', '6.9', '186.186', '32.64',
                '36.48', '3.40', '91.91', '2.33', '1.5', '31.64', '10.13', '49.11', '35.64', '104.65', '215.215',
                '255.173', '1.29', '89.100', '113.108', '31.41', '32.83', '19.2', '255.74', '253.64', '8.111', '23.13',
                '51.50', '147.64', '97.72', '210.210', '146.64', '255.175', '7.128', '243.84', '99.65', '38.64',
                '109.47', '106.69', '77.121', '251.252', '17.183', '105.103', '99.36', '130.55', '9.6', '105.110',
                '139.226', '255.248', '189.189', '3.130', '110.116', '158.158', '69.98', '80.65', '100.108', '245.245',
                '255.243', '3.29', '255.111', '97.66', '11.7', '3.2', '55.2', '252.252', '17.64', '102.207', '0.128',
                '108.103', '75.73', '32.67', '49.48', '64.0', '75.95', '13.10', '10.111', '86.66', '70.107', '219.172',
                '46.114', '22.4', '18.64', '101.115', '89.66', '103.75', '113.65', '116.112', '90.84', '15.28', '255.234',
                '181.67', '10.115', '255.188', '101.116', '122.124', '176.64', '229.229', '24.48', '65.12', '255.166',
                '43.64', '32.32', '111.92', '255.253', '209.90', '77.99', '100.101', '137.22', '80.114', '17.213',
                '95.105', '47.99']

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    for i in range(len(file_bytes) - (n - 1)):

        # ex) if 3 gram, seq is '13.15.255'
        seq = ".".join(([str(v) for v in file_bytes[i:i + n]]))

        try:
            feature_list[seq] += 1
        except:
            pass

    return feature_list


def get3gram(file_name):
    root_path = '../'
    n = 3

    # column names
    colnames = []

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    for i in range(len(file_bytes) - (n - 1)):

        # ex) if 3 gram, seq is '13.15.255'
        seq = ".".join(([str(v) for v in file_bytes[i:i + n]]))

        try:
            feature_list[seq] += 1
        except:
            pass

    return feature_list


def get4gram(file_name):
    root_path = '../'
    n = 4

    # column names
    colnames = []

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    for i in range(len(file_bytes) - (n - 1)):

        # ex) if 3 gram, seq is '13.15.255'
        seq = ".".join(([str(v) for v in file_bytes[i:i + n]]))

        try:
            feature_list[seq] += 1
        except:
            pass

    return feature_list


def getWholeLine(file_name):
    root_path = '../'

    # column names
    colnames = []

    # make feature list (dict form)
    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    for line in np.resize(file_bytes, (len(file_bytes) // 16, 16)):

        seq = '.'.join([str(v) for v in line])

        try:
            feature_list[seq] += 1
        except:
            pass

    return feature_list