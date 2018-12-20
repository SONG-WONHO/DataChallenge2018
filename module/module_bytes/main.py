# module
import multiprocessing
import pandas as pd
import time

# feature
import feature.ngram as ngram
import feature.strings as strings
import feature.images as images

# custom utils
import utils_c

'''
3gram, 4gram, wholelinegram
'''


def main():

    # make result directory
    utils_c.make_result_dir()

    # constant
    NUM_OF_PROCESSOR = int(input("please input the number of processor: "))

    # get file name - ext:vir
    file_names = utils_c.get_file_list('../', 'vir')

    print("starting bytes code analysis")
    print("num of bytes code: {}".format(len(file_names)))
    print("num of processor: {}".format(NUM_OF_PROCESSOR))

    # job list
    jobs = [strings.getLengthCnt, strings.getSymbol, strings.getMisc, images.haralick, ngram.get1gram, ngram.get2gram]

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
        if job.__name__ == 'haralick':
            data.to_csv('./result/feature_bytes_img_haralick.csv')
        elif job.__name__ == 'getLengthCnt':
            data.to_csv('./result/feature_bytes_str_len.csv')
        elif job.__name__ == 'getSymbol':
            data.to_csv('./result/feature_bytes_str_sym.csv')
        elif job.__name__ == 'getMisc':
            data.to_csv('./result/feature_bytes_str_misc.csv')
        elif job.__name__ == 'get1gram':
            data.to_csv('./result/feature_bytes_ngram_1gram.csv')
        elif job.__name__ == 'get2gram':
            data.to_csv('./result/feature_bytes_ngram_2gram.csv')


if __name__ == '__main__':
    main()
