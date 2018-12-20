#modlue
import os
import time
import multiprocessing
import subprocess

import utils_c


#functions
def op(file_name):
    subprocess.call(["ida", "-B", "../" + file_name])
    time.sleep(0.1)
    return


if __name__ == '__main__':

    # global variables
    NUM_OF_PROCESSOR = int(input("please input the num of processor: "))

    #start time
    start = time.time()

    #get file name - ext:vir
    file_names = utils_c.get_file_list('../', 'vir')

    pool = multiprocessing.Pool(NUM_OF_PROCESSOR)
    pool.map(op, file_names)

    #get file name - ext:asm
    file_names = utils_c.get_file_list('../', 'asm')

    #make asm directory
    try:
        os.makedirs('./asm/')
    except:
        pass

    #move asm file to asm directory
    for file_name in file_names:
        try:
            os.rename('../' + file_name, './asm/' + file_name)
        except:
            pass

    #end time
    end = time.time()

    #execution time
    exec_time = int(end - start)
    print("hour: {}, minute: {}, second: {}".format(exec_time//3600, exec_time%3600 // 60, exec_time%60))