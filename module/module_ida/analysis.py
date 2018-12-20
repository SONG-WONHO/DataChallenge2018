# module
import idaapi
import idc
import idautils

import os
import csv
import json

import pefile


# get hash
def getHash(root_path):

    with open(root_path + 'hash.txt', 'w') as f:
        try:
            hash_md5 = idautils.GetInputFileMD5()
        except:
            hash_md5 = "error"

        f.write(hash_md5)


# get file size
def getBinFileSize(root_path, file_name, ext):

    with open(root_path + 'bin_size.txt', 'w') as f:
        try:
            size = str(os.path.getsize('./' + file_name + '.' + ext))
        except:
            size = "error"
            
        f.write(size)


# get address of first line
def getAddressOfFirstLine(root_path):

    with open(root_path + 'first_address.txt', 'w') as f:

        try:
            address_of_first_line = str(hex(idc.MinEA()))
        except:
            address_of_first_line = "error"

        f.write(address_of_first_line)


# features that related asm lines
def getFeatureWithLines(root_path):

    '''
    - number of lines
    - opcode
    - register value
    - data definition
    '''

    # file handler
    wr_number_of_lines = open(root_path + 'number_of_lines.txt', 'w')
    wr_opcode = open(root_path + 'opcode.txt', 'w')
    wr_register = open(root_path + 'register.txt', 'w')
    wr_dd = open(root_path + 'data_define.txt', 'w')
    wr_instruction = open(root_path + 'instruction.txt', 'w')

    # start address
    temp = idc.MinEA()

    # local variable related feature
    number_of_lines = 0
    opcode_list = []
    register_list = []
    dd_list = []
    instruction_list = []

    
    # when meets end address, break loop
    # set limit 10000000
    for _ in range(10000000):

        # number of lines
        number_of_lines = number_of_lines + 1

        # get opcode
        opcode_list.append(str(idc.GetMnem(temp)))

        # get register
        for i in range(8):
            
            # get operand type
            operand_type = idc.GetOpType(temp, i)

            # define o_reg 1
            if operand_type == 1:

                operand = idc.GetOpnd(temp, i)
                
                # remove noise value
                if 0 < len(operand) < 4:
                    register_list.append(operand)

            # define o_void 0, define bad_operand -1
            if operand_type == 0 or operand_type == -1:
                break

        # get data define
        try:
            # get opcode
            dd = idc.GetDisasm(temp).split()[0].lower()
            
            # if dd is data define, then append them in list
            if dd == "dd" or dd == "dw" or dd == dd == "db":
                dd_list.append(dd)

        except:
            pass

        # get instruction
        if str(idc.GetMnem(temp)) != "":

            # format example: ['mov', 'REG', 'REG']
            instruction = []

            # opcode
            instruction.append(str(idc.GetMnem(temp)))

            # operand
            for i in range(8):

                # o_void=0, o_reg=1, o_mem=2, o_phrase=3, o_displ=4, o_imm=5, o_far=6, o_near=7
                operand_type = idc.GetOpType(temp, i)

                # bad addr or void
                if operand_type == -1 or operand_type == 0:
                    break

                # reg    
                elif operand_type == 1:
                    instruction.append("REG")
                
                # mem
                elif operand_type == 2 or operand_type == 3 or operand_type == 4:
                    instruction.append("MEM")
                
                # immediate value
                elif operand_type == 5:
                    instruction.append("VALUE")
                
                # address
                elif operand_type == 6 or operand_type == 7:
                    instruction.append("ADDR")
                
                # etc
                else:
                    instruction.append("ETC")

            instruction_list.append(".".join(instruction))

        # next address
        temp = idc.NextHead(temp)

        if temp > idc.MaxEA() - 1:
            break

    wr_number_of_lines.write(str(number_of_lines))
    wr_opcode.write(",".join(opcode_list))
    wr_register.write(",".join(register_list))
    wr_dd.write(",".join(dd_list))
    wr_instruction.write(",".join(instruction_list))


# get pe info
def getPEInfo(root_path):

    with open(root_path + 'pe.json', 'w') as f:

        pe_info = {}

        pe = pefile.PE('./' + idc.GetInputFile())

        #file header
        pe_info["Machine"] = pe.FILE_HEADER.Machine 
        pe_info["NumberOfSections"] = pe.FILE_HEADER.NumberOfSections
        pe_info["TimeDateStamp"] = pe.FILE_HEADER.TimeDateStamp
        pe_info["PointerToSymbolTable"] = pe.FILE_HEADER.PointerToSymbolTable
        pe_info["NumberOfSymbols"] = pe.FILE_HEADER.NumberOfSymbols
        pe_info["SizeOfOptionalHeader"] = pe.FILE_HEADER.SizeOfOptionalHeader
        pe_info["Characteristics"] = pe.FILE_HEADER.Characteristics

        #optional header
        pe_info["MajorLinkerVersion"] = pe.OPTIONAL_HEADER.MajorLinkerVersion
        pe_info["MinorLinkerVersion"] = pe.OPTIONAL_HEADER.MinorLinkerVersion
        pe_info["SizeOfCode"] = pe.OPTIONAL_HEADER.SizeOfCode
        pe_info["SizeOfInitializedData"] = pe.OPTIONAL_HEADER.SizeOfInitializedData
        pe_info["SizeOfUninitializedData"] = pe.OPTIONAL_HEADER.SizeOfUninitializedData
        pe_info["AddressOfEntryPoint"] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        pe_info["ImageBase"] = pe.OPTIONAL_HEADER.ImageBase
        pe_info["SectionAlignment"] = pe.OPTIONAL_HEADER.SectionAlignment
        pe_info["FileAlignment"] = pe.OPTIONAL_HEADER.FileAlignment
        pe_info["MajorOperatingSystemVersion"] = pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
        pe_info["MinorOperatingSystemVersion"] = pe.OPTIONAL_HEADER.MinorOperatingSystemVersion
        pe_info["MajorImageVersion"] = pe.OPTIONAL_HEADER.MajorImageVersion
        pe_info["MinorImageVersion"] = pe.OPTIONAL_HEADER.MinorImageVersion
        pe_info["MajorSubsystemVersion"] = pe.OPTIONAL_HEADER.MajorSubsystemVersion
        pe_info["MinorSubsystemVersion"] = pe.OPTIONAL_HEADER.MinorSubsystemVersion
        pe_info["SizeOfImage"] = pe.OPTIONAL_HEADER.SizeOfImage
        pe_info["SizeOfHeaders"] = pe.OPTIONAL_HEADER.SizeOfHeaders
        pe_info["CheckSum"] = pe.OPTIONAL_HEADER.CheckSum
        pe_info["SizeOfStackReserve"] = pe.OPTIONAL_HEADER.SizeOfStackReserve
        pe_info["SizeOfStackCommit"] = pe.OPTIONAL_HEADER.SizeOfStackCommit
        pe_info["SizeOfHeapReserve"] = pe.OPTIONAL_HEADER.SizeOfHeapReserve
        pe_info["SizeOfHeapCommit"] = pe.OPTIONAL_HEADER.SizeOfHeapCommit
        pe_info["NumberOfRvaAndSizes"] = pe.OPTIONAL_HEADER.NumberOfRvaAndSizes

        #custom - https://github.com/ClickSecurity/data_hacking/blob/master/pefile_classification/pe_features.py
        pe_info["DebugSize"] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
        pe_info["IatRva"] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
        pe_info["ExportSize"] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
        try:
            pe_info["GeneratedCheckSum"] = pe.generate_checksum()
        except:
            pe_info["GeneratedCheckSum"] = 0
        try:
            pe_info["TotalSizePE"] = len(pe.__data__)
        except:
            pe_info["TotalSizePE"] = 0
        try:
            pe_info["PeExe"] = 1 if pe.is_exe() else 0
        except:
            pe_info["PeExe"] = 2
        try:
            pe_info["PeDriver"] = 1 if pe.is_driver() else 0
        except:
            pe_info["PeDriver"] = 2
        try:
            pe_info["PeDll"] = 1 if pe.is_dll() else 0
        except:
            pe_info["PeDll"] = 2

        # section header
        pe_info["Sections"] = {}

        for section in pe.sections:
            pe_info["Sections"][str(section.Name)] = {}
            pe_info["Sections"][section.Name]["Misc"] = section.Misc
            pe_info["Sections"][section.Name]["Misc_PhysicalAddress"] = section.Misc_PhysicalAddress
            pe_info["Sections"][section.Name]["Misc_VirtualSize"] = section.Misc_VirtualSize
            pe_info["Sections"][section.Name]["VirtualAddress"] = section.VirtualAddress
            pe_info["Sections"][section.Name]["SizeOfRawData"] = section.SizeOfRawData
            pe_info["Sections"][section.Name]["PointerToRawData"] = section.PointerToRawData
            pe_info["Sections"][section.Name]["SizeOfRawData"] = section.SizeOfRawData
            pe_info["Sections"][section.Name]["Entropy"] = section.get_entropy()

        json.dump(pe_info, f)


# get section info
def getSectionInfo(root_path):

    with open(root_path + 'section.csv', 'w') as f:

        wr = csv.writer(f)
        wr.writerow(['name', 'align', 'combination', 'flags', 'selector', 'type', 'r', 'w', 'x', 'size'])

        # segment objects
        for seg in idautils.Segments():

            # Segment Name
            try:
                name = idc.SegName(seg)
            except:
                name = "error"

            # Segment Align
            try:
                align = idc.GetSegmentAttr(seg, SEGATTR_ALIGN)
            except:
                align = "error"

            # Segment Combination
            try:
                combination = idc.GetSegmentAttr(seg, SEGATTR_COMB)
            except:
                combination = "error"

            # Segment Flags
            try:
                flags = idc.GetSegmentAttr(seg, SEGATTR_FLAGS)
            except:
                flags = "error"

            # Segment Selector
            try:
                selector = idc.GetSegmentAttr(seg, SEGATTR_SEL)
            except:
                selector = "error"

            # Segment Type
            try:
                seg_type = idc.GetSegmentAttr(seg, SEGATTR_TYPE)
            except:
                seg_type = "error"

            # Segment Permission
            try:
                perm_r = 0
                perm_w = 0
                perm_x = 0

                perm = idc.GetSegmentAttr(seg, SEGATTR_PERM)

                if perm == 1:
                    perm_x = 1

                elif perm == 2:
                    perm_w = 1

                elif perm == 4:
                    perm_r = 1

                elif perm == 3:
                    perm_x = 1
                    perm_w = 1

                elif perm == 6:
                    perm_w = 1
                    perm_r = 1

                elif perm == 5:
                    perm_x = 1
                    perm_r = 1

                elif perm == 7:
                    perm_r = 1
                    perm_w = 1
                    perm_x = 1

            except:
                perm_r = "error"
                perm_w = "error"
                perm_x = "error"

            # Segment Size
            try:
                size = idc.GetSegmentAttr(seg, SEGATTR_END) - idc.GetSegmentAttr(seg, SEGATTR_START)
            except:
                size = "error"

            wr.writerow([name, align, combination, flags, selector, seg_type, perm_r, perm_w, perm_x, size])


# get import table information
def getDllApiInfo(root_path):

    with open(root_path + 'dll.json', 'w') as f:

        # total dll count
        dll_num = idaapi.get_import_module_qty()
        dll_list = dict()

        for i in range(dll_num):

            # get dll name
            dll_name = idaapi.get_import_module_name(i)

            if not dll_name:
                continue

            dll_list[dll_name] = []

            # get api function of each dll name
            def imp_cb(ea, name, ord):
                if not name:
                    dll_list[dll_name].append("error")
                else:
                    dll_list[dll_name].append(name)

                return True

            idaapi.enum_import_names(i, imp_cb)

        #return json format
        json.dump(dll_list, f)


# get function info
def getFuncInfo(root_path):

    with open(root_path + 'function.json', 'w') as f:

        function_list = {"function_all": [], "function_lib": [], "function_hidden":[], "function_noret": [], "function_thunk": [], "function_static": []}

        for func in idautils.Functions():

            # function name
            func_name = idc.GetFunctionName(func)

            # add all
            function_list['function_all'].append(func_name)

            # flags
            flags = idc.GetFunctionFlags(func)

            # library
            if flags & FUNC_LIB:

                function_list['function_lib'].append(idc.GetFunctionName(func))

            # hidden
            if flags & FUNC_HIDDEN:

                function_list['function_hidden'].append(idc.GetFunctionName(func))

            #no return
            if flags & FUNC_NORET:

                function_list['function_noret'].append(idc.GetFunctionName(func))

            #thunk
            if flags & FUNC_THUNK:

                function_list['function_thunk'].append(idc.GetFunctionName(func))

            #static
            if flags & FUNC_STATIC:

                function_list['function_static'].append(idc.GetFunctionName(func))

        json.dump(function_list, f)


# wait
idaapi.autoWait()

# get file name
file_name = idc.GetInputFile().split(".")[0]
ext = idc.GetInputFile().split(".")[1]

# root path
root_path = './module/result/' + file_name + '/'

getHash(root_path)
getBinFileSize(root_path, file_name, ext)
getAddressOfFirstLine(root_path)
getFeatureWithLines(root_path)
getPEInfo(root_path)
getSectionInfo(root_path)
getDllApiInfo(root_path)
getFuncInfo(root_path)

# turn off ida pro
idc.Exit(0)