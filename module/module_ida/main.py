# modlue
import time
import multiprocessing
import os

# custom utils
import utils_c


# functions
def op(file_name):

    os.system("ida -A -c -S./module/analysis.py ../" + file_name)

    '''
    ======== old version ========

    import subprocess
    subprocess.call(["ida", "-A", "-c", "-S./module/analysis.py", "../" + file_name])
    '''
    
    time.sleep(0.1)
    return


if __name__ == '__main__':

    # global variables
    NUM_OF_PROCESSOR = int(input("please input the num of processor: "))

    # start time
    start = time.time()

    # get file name - ext:vir
    file_names = utils_c.get_file_list('../', 'vir')

    print("start malware analysis")
    print("num of malware: {}".format(len(file_names)))
    print("num of processor: {}".format(NUM_OF_PROCESSOR))

    # make directory
    utils_c.make_dir(file_names)

    # processor pool
    pool = multiprocessing.Pool(NUM_OF_PROCESSOR)
    pool.map(op, file_names)

    # end time
    end = time.time()

    # execution time
    exec_time = int(end - start)
    print("hour: {}, minute: {}, second: {}".format(exec_time//3600, exec_time%3600 // 60, exec_time%60))