# module
import multiprocessing
import pandas as pd
import time

# custom utils
import utils_c


def get_asm_img(file_name):
    root_path = '../'

    colnames = ['asm_img_' + str(i+1) for i in range(1000)]

    feature_list = {'hash': file_name}
    for v in colnames:
        feature_list[v] = 0

    file_path = root_path + file_name
    file_bytes = [v for v in open(file_path, 'rb').read()]

    try:
        for i in range(1000):
            feature_list['asm_img_' + str(i+1)] = file_bytes[i]

    except:
        pass

    return feature_list


def main():

    # make result directory
    utils_c.make_result_dir()

    # constant
    NUM_OF_PROCESSOR = int(input("please input the number of processor: "))

    # get file name - ext:vir
    file_names = utils_c.get_file_list('../', 'asm')

    print("starting bytes code analysis")
    print("num of asm code: {}".format(len(file_names)))
    print("num of processor: {}".format(NUM_OF_PROCESSOR))

    # job list
    jobs = [get_asm_img]

    # processor pool
    pool = multiprocessing.Pool(processes=NUM_OF_PROCESSOR)

    for job in jobs:

        # start time
        start = time.time()

        feature_lists = pool.map(job, file_names)

        # execution time
        exec_time = int(time.time() - start)
        print("[{}] hour: {}, minute: {}, second: {}".format(job.__name__, exec_time // 3600, exec_time % 3600 // 60, exec_time % 60))

        # dict list to data frame
        data = pd.DataFrame(feature_lists)
        data = data.set_index('hash')

        # to csv

        data.to_csv('./result/feature_asm_img.csv')


if __name__ == '__main__':
    main()
