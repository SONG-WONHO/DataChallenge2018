# default module
import os
import time
import multiprocessing
import pandas as pd

# feature
import feature.pe as pe
import feature.dll as dll
import feature.api as api
import feature.section as section
import feature.function as func
import feature.etc as etc
import feature.register as register
import feature.data_define as dd
import feature.opcode as opcode
import feature.instruction as inst

# custom utils
import utils_c


def main():
    # make result directory
    utils_c.make_result_dir()

    # constant
    NUM_OF_PROCESSOR = int(input("please input number of processor: "))
    ROOT_PATH = '../'

    # get dir name
    dir_names = [f for f in os.listdir(ROOT_PATH) if not f == 'module_asm']

    print("create asm features.\n")
    print("number of processor: {}".format(NUM_OF_PROCESSOR))

    # job list
    jobs = [pe.get_pe_info,
            dll.get_dll_freq, api.get_api_freq,
            section.get_section_name_freq,
            section.get_exec_section_name_freq,
            section.get_section_info,
            section.get_section_entropy,
            func.get_func_cnt,
            etc.get_etc_info,
            register.get_register_freq,
            register.get_register_2g,
            register.get_register_3g,
            register.get_register_4g,
            dd.get_dd_freq,
            opcode.get_opcode_freq,
            opcode.get_opcode_1g,
            opcode.get_opcode_2g,
            opcode.get_opcode_3g,
            opcode.get_opcode_4g,
            inst.get_instruction_1g,
            inst.get_instruction_2g,
            inst.get_instruction_3g,
            inst.get_instruction_4g]


    # processor pool
    pool = multiprocessing.Pool(processes=NUM_OF_PROCESSOR)

    for job in jobs:

        # start time
        start = time.time()

        feature_lists = pool.map(job, dir_names)

        # execution time
        exec_time = int(time.time() - start)
        print("[{}] hour: {}, minute: {}, second: {}".format(job.__name__, exec_time // 3600, exec_time % 3600 // 60, exec_time % 60))

        # dict list to data frame
        data = pd.DataFrame(feature_lists)
        data = data.set_index('hash')

        # temp
        # print(data)

        # to csv
        if job.__name__ == 'get_pe_info':
            data.to_csv('./result/feature_asm_pe_info.csv')
        elif job.__name__ == 'get_dll_freq':
            data.to_csv('./result/feature_asm_dll_freq.csv')
        elif job.__name__ == 'get_api_freq':
            data.to_csv('./result/feature_asm_api_freq.csv')
        elif job.__name__ == 'get_section_name_freq':
            data.to_csv('./result/feature_asm_section_name_freq.csv')
        elif job.__name__ == 'get_exec_section_name_freq':
            data.to_csv('./result/feature_asm_exec_section_name_freq.csv')
        elif job.__name__ == 'get_section_info':
            data.to_csv('./result/feature_asm_section_info.csv')
        elif job.__name__ == 'get_section_entropy':
            data.to_csv('./result/feature_asm_section_entropy.csv')
        elif job.__name__ == 'get_func_cnt':
            data.to_csv('./result/feature_asm_func_cnt.csv')
        elif job.__name__ == 'get_etc_info':
            data.to_csv('./result/feature_asm_etc_info.csv')
        elif job.__name__ == 'get_register_freq':
            data.to_csv('./result/feature_asm_register_freq.csv')
        elif job.__name__ == 'get_dd_freq':
            data.to_csv('./result/feature_asm_dd_freq.csv')
        elif job.__name__ == 'get_opcode_freq':
            data.to_csv('./result/feature_asm_opcode_freq.csv')
        elif job.__name__ == 'get_opcode_1g':
            data.to_csv('./result/feature_asm_opcode_1g.csv')
        elif job.__name__ == 'get_opcode_2g':
            data.to_csv('./result/feature_asm_opcode_2g.csv')
        elif job.__name__ == 'get_opcode_3g':
            data.to_csv('./result/feature_asm_opcode_3g.csv')
        elif job.__name__ == 'get_opcode_4g':
            data.to_csv('./result/feature_asm_opcode_4g.csv')
        elif job.__name__ == 'get_register_2g':
            data.to_csv('./result/feature_asm_register_2g.csv')
        elif job.__name__ == 'get_register_3g':
            data.to_csv('./result/feature_asm_register_3g.csv')
        elif job.__name__ == 'get_register_4g':
            data.to_csv('./result/feature_asm_register_4g.csv')
        elif job.__name__ == 'get_instruction_1g':
            data.to_csv('./result/feature_asm_inst_1g.csv')
        elif job.__name__ == 'get_instruction_2g':
            data.to_csv('./result/feature_asm_inst_2g.csv')
        elif job.__name__ == 'get_instruction_3g':
            data.to_csv('./result/feature_asm_inst_3g.csv')
        elif job.__name__ == 'get_instruction_4g':
            data.to_csv('./result/feature_asm_inst_4g.csv')


if __name__ == '__main__':
    main()