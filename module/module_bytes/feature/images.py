import numpy as np
import mahotas


def haralick(file_name):
    root_path = '../'

    # column names
    colnames = ['imgHaralick_' + str(i) for i in range(52)]

    # file path
    file_path = root_path + file_name

    # bytes file
    file_bytes = [v for v in open(file_path, 'rb').read()]

    try:
        # bytes file to img array
        img_array = np.resize(file_bytes, (len(file_bytes) // 16, 16))

        b = int((img_array.shape[0] * 16) ** (0.5))
        b = 2 ** (int(np.log(b) / np.log(2)) + 1)
        a = int(img_array.shape[0] * 16 / b)

        img_array = img_array[:int(a * b / 16), :]
        img_array = np.reshape(img_array, (a, b))

    # if error, default value
    except:
        img_array = np.array([[1, 1], [1, 1]])

    # get haralick features
    features = np.squeeze(mahotas.features.haralick(img_array))
    features = [round(d, 3) for v in features for d in v]

    # feature list
    feature_list = {'hash': file_name}

    for j, v in enumerate(colnames):
        feature_list[v] = features[j]

    temp_1 = ['imgHaralick_12', 'imgHaralick_11', 'imgHaralick_8', 'imgHaralick_45', 'imgHaralick_32', 'imgHaralick_19',
             'imgHaralick_31', 'imgHaralick_5', 'imgHaralick_38', 'imgHaralick_44', 'imgHaralick_18', 'imgHaralick_15',
             'imgHaralick_6', 'imgHaralick_2', 'imgHaralick_10', 'imgHaralick_51', 'imgHaralick_41', 'imgHaralick_21',
             'imgHaralick_25', 'imgHaralick_47', 'imgHaralick_28', 'imgHaralick_7', 'imgHaralick_1', 'imgHaralick_29',
             'imgHaralick_4', 'imgHaralick_37', 'imgHaralick_3', 'imgHaralick_42', 'imgHaralick_34', 'imgHaralick_27',
             'imgHaralick_33', 'imgHaralick_40', 'imgHaralick_14', 'imgHaralick_16', 'imgHaralick_50', 'imgHaralick_24',
             'imgHaralick_36', 'imgHaralick_46', 'imgHaralick_20', 'imgHaralick_49', 'imgHaralick_23', 'imgHaralick_30',
             'imgHaralick_43', 'imgHaralick_0']

    temp_2 = {'hash': file_name}

    for v in temp_1:
        temp_2[v] = feature_list[v]

    return temp_2
