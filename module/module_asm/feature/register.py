def get_register_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/register.txt"

    colnames = ['ah', 'al', 'ax', 'bh', 'bl', 'bp', 'bx', 'ch', 'cl', 'cs', 'cx',
                'dh', 'di', 'dl', 'ds', 'dx', 'eax', 'ebp', 'ebx', 'ecx', 'edi',
                'edx', 'es', 'esi', 'esp', 'fs', 'gs', 'si', 'ss']

    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        register_list = open(file_path, 'r').read().split(',')

        for register in register_list:
            try:
                feature_list[register] += 1

            except:
                pass

    except:
        pass

    return feature_list


def get_register_2g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/register.txt"

    colnames = ['3Fh.0', 'ebp.eax', 'ecx.ecx', 'ebp.ebp', '1.1', '3Fh.3Fh', 'eax.eax', 'esp.eax', 'edi.ebp', 'ecx.esi', 'ebp.edi', 'ebp.ecx', 'edi.eax', 'esi.ecx', 'edi.ecx', 'eax.edi', 'eax.ebp', 'eax.ebx', 'ecx.eax', 'ebp.esi', 'esp.esi', 'edi.edi', 'esi.ebp', 'edx.eax', 'ecx.cx', 'ebx.esp', 'ecx.edx', 'ecx.edi', 'esi.ebx', '0.3Fh', 'eax.ecx', 'esi.esp', 'esp.edi', 'esi.eax', 'esi.edi', 'edi.esi', '0.0', 'eax.esp', 'ebx.eax', 'ebp.esp', 'edx.ecx', 'eax.esi', 'esi.esi', 'ecx.ebp', '43h.43h', 'ebx.ecx', 'ecx.esp', 'esp.ebp', 'al.al', 'esp.esp', 'ebp.ebx', 'eax.cl', 'ebx.ebx', 'eax.al', 'al.eax', '2Eh.2Eh', 'edi.ebx', '5Fh.5Fh', '44h.44h', 'esp.ebx', 'ebx.esi', 'ebx.edi', 'eax.edx', '0.53h', '4.4', 'ecx.ebx', 'al.bl', 'edi.al', 'esp.ecx', 'al.edx', 'edi.edx', 'ebx.ebp', 'edx.edx', 'cl.eax', 'cx.ecx', 'al.ecx', 'eax.ax', 'bl.al', '49h.49h', '10h.10h', 'edx.ebx', '53h.0', 'ebx.edx', 'esi.edx', 'cl.edx', '8Bh.8Bh', 'edx.edi', 'esi.al', 'ecx.al', 'edx.esi', 'bl.eax', 'al.esi', 'ax.eax', 'al.ebx', 'ebx.al', 'esp.edx', 'edx.al', 'cl.cl', 'ecx.bl', 'cl.ecx', 'edi.esp', '47h.47h', 'ebp.edx', 'cx.eax', '52h.52h', 'edx.esp', 'eax.bl', 'ecx.dl', 'ecx.ax', 'dl.eax', '45h.45h', 'al.cl', 'dl.al', '4.2', 'ebx.cl', 'ax.edx', 'ax.ax', 'cl.al', 'edx.dl', '8Dh.eax', '3.8', '8Bh.ebp', 'ebx.bl', 'dl.dl', 'ebp.8Bh', 'esi.bl', 'al.esp', 'ax.dx', 'cx.cx', '53h.53h', 'esp.al', 'edx.ebp', 'ax.ecx', 'bl.bl', 'edx.cl', '0.6', 'dl.ecx', 'eax.cx', 'dx.eax', 'dx.ax', 'edi.cl', 'ebp.8Dh', 'ecx.cl', 'bl.ecx', 'dh.al', 'cl.dl', 'eax.dx', '8Dh.ebx', 'bl.esi', 'eax.dl', '1.0', 'esi.cl', '65h.65h', 'bl.edi', 'ebx.8Dh', '8Dh.ebp', 'dl.edx', '2.1', 'eax.8Dh', 'ax.ah', '66h.66h', '0.1', '0Ch.0Ch', 'ebx.8Bh', 'esi.dl', '89h.89h', 'ch.dl', 'dx.dx', '63h.63h', 'ax.cx', '46h.46h', '4Dh.4Dh', '42h.42h', '0.69h', '3.2', '69h.69h', 'bl.cl', 'dl.cl', 'ax.ebp', 'ebx.dl', 'ah.ax', '8Bh.ebx', 'al.dh', 'dl.bl', '69h.0', '50h.50h', 'bl.edx', 'bx.bx', 'dh.eax', '20h.0', '3.0', '57h.57h', '2Dh.2Dh', '41h.41h', 'eax.dh', '63h.0', '2.2', '3.1', '0.8', '8Ah.8Ah']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        register_list = open(file_path, 'r').read().split(',')

        for i in range(len(register_list) - (2 - 1)):
            seq = '.'.join([str(v) for v in register_list[i: i + 2]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_register_3g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/register.txt"

    colnames = ['eax.eax.eax', 'ebp.ebp.eax', 'eax.ebp.eax', '3Fh.3Fh.3Fh', 'ecx.ecx.eax', 'edi.edi.ebp', 'ecx.ecx.ecx', 'ebp.esp.esp', 'eax.edi.eax', 'ebp.edi.edi', 'edi.edi.eax', 'esi.ebx.esp', 'ecx.esi.esp', 'ecx.eax.eax', 'ecx.ecx.edi', 'ecx.edi.eax', 'esi.esp.eax', '3Fh.0.3Fh', 'ebp.ebp.ebp', 'edi.ebp.ebp', 'ebp.ebp.esp', 'edi.esi.ebp', 'eax.ecx.ecx', 'ebp.esp.eax', 'eax.eax.cl', 'esp.eax.eax', 'ebx.esp.eax', '5Fh.5Fh.5Fh', 'ecx.ecx.edx', 'eax.eax.ecx', 'ebp.ebp.edi', 'edi.eax.edi', 'eax.esp.ebx', 'eax.eax.al', 'eax.ecx.esi', 'eax.eax.ebp', 'ebp.ebx.esp', 'esp.esp.eax', 'eax.edi.ecx', 'al.al.al', 'ebx.esp.ebp', 'ax.edx.eax', 'edx.ecx.ecx', 'eax.esi.ecx', 'esi.esi.edi', 'eax.esi.ebx', 'eax.eax.edi', 'ecx.edx.ecx', 'ecx.edi.edi', 'edi.esi.ebx', 'ebp.eax.eax', 'esi.ecx.ecx', 'esi.eax.ecx', 'esi.edi.edi', 'edi.eax.ebx', 'eax.eax.esp', 'esi.esi.esi', 'eax.esp.eax', 'ebx.eax.eax', 'edi.eax.esp', 'eax.edi.esi', 'esp.ebp.ebp', 'edi.ecx.ecx', 'eax.esi.esp', 'edi.eax.esi', 'ecx.esp.eax', 'ecx.esp.esp', 'edi.eax.ecx', 'esi.eax.esi', 'esi.ebx.eax', 'eax.eax.ebx', 'ecx.esi.eax', 'esi.edi.ecx', 'edx.eax.ax', 'eax.edi.edi', 'eax.esi.esi', 'eax.ax.edx', 'esp.esi.edi', 'eax.eax.esi', 'ecx.ecx.ebp', 'ebp.eax.esp', 'edi.edi.esi', 'ebp.esp.ecx', 'eax.al.al', 'esp.eax.ecx', 'esp.esi.esi', 'edi.eax.eax', 'edi.esi.edi', 'eax.ebx.edi', 'ecx.al.al', 'ecx.esi.ecx', 'esp.edi.edi', 'al.eax.esi', 'eax.esi.eax', 'ebx.eax.esi', 'edi.esi.ecx', 'esi.eax.eax', 'ebp.esi.esi', 'ebp.eax.ebx', '52h.52h.52h', 'eax.edi.esp', 'ecx.eax.esi', 'edi.ebx.eax', 'edx.eax.eax', 'ebx.esi.edi', 'ecx.esi.esi', 'edi.edi.ecx', 'ecx.edx.edx', 'esi.esi.eax', 'edx.al.al', 'ecx.ecx.esp', 'ecx.esi.edi', 'eax.eax.edx', 'esi.ebx.esi', 'al.eax.eax', 'ebx.edi.eax', 'esp.esp.ebx', 'eax.ebx.eax', 'esi.edi.eax', 'eax.al.eax', 'esi.edi.esp', 'eax.ecx.edi', '45h.45h.45h', 'edx.ecx.edx', 'ecx.ecx.esi', 'ecx.eax.edi', 'al.al.eax', 'ebx.edi.ecx', 'edi.edi.ebx', 'al.esi.ecx', 'edx.edx.ecx', 'eax.esi.edi', 'esi.eax.edi', '53h.53h.53h', 'esi.eax.esp', 'eax.ebx.ebx', 'eax.ecx.eax', 'ebx.ebx.eax', 'eax.ebx.al', 'ebx.esi.ebx', 'edi.edi.edi', 'ebx.eax.ebx', 'eax.ebx.esi', 'ebx.ebx.ebx', 'esi.eax.ebx', 'ebx.esi.esi', 'esi.esp.ebp', 'ecx.ecx.ebx', 'eax.edx.eax', 'ebx.ecx.ecx', 'edx.ecx.al', 'ebx.ebx.ecx', 'ecx.eax.ecx', 'edx.ecx.eax', 'eax.edi.ebx', 'ebx.edi.edi', 'edi.esi.esi', 'esp.edx.eax', 'eax.dl.eax', 'cl.eax.eax', 'edi.ecx.edx', 'eax.edx.edx', 'edx.edx.edx', 'edi.ecx.edi', '43h.43h.43h', 'al.eax.al', 'esp.eax.esi', 'esp.ecx.eax', 'esi.edi.esi', 'eax.ebp.edi', 'ecx.edi.esi', 'edx.eax.edx', 'ebx.esi.eax', 'dl.eax.eax', 'esi.esi.ecx', 'edx.edx.eax', '4.4.4', 'eax.ebp.ebp', 'dl.eax.edx', 'esi.edi.ebx', 'edx.eax.ecx', 'eax.edx.ecx', 'ebx.ebx.esi', 'esi.ebx.ebx', 'edi.ebx.ebx', 'edi.ecx.eax', 'esi.esi.esp', 'esi.ecx.esi', 'esp.esp.ebp', 'esp.ebx.esi', 'esi.esp.edi', 'ebx.eax.edi', 'eax.ebx.cl', 'esi.esi.ebp', 'al.al.ecx', 'esp.eax.ebx', 'ebp.edi.esi', 'edi.esi.eax', 'esi.ebp.eax', 'esi.edi.ebp', 'ecx.eax.ebx', 'ebp.8Bh.8Bh', 'esp.ecx.ecx', 'ebx.ebp.edi', 'esp.eax.edi', 'esi.ecx.eax', 'esp.ebx.ebx', 'eax.ax.eax', 'ecx.eax.edx', 'ecx.edx.eax', 'ecx.edi.ecx', 'ebx.ebp.ebp', 'ecx.ebx.ebx', 'edi.ebx.edi', 'eax.esp.esp', 'esi.ebx.ecx', 'eax.ecx.edx', '8Dh.ebx.esi', 'eax.ebx.ecx', 'ebp.esp.ebx', 'ecx.al.esi', 'al.eax.ebx', 'edi.edx.eax', 'eax.esp.esi', 'ebx.ecx.eax', 'ebx.eax.esp', 'esi.esi.ebx', 'edx.edx.esi', 'ebx.edi.ebx', 'ebx.al.al', 'esp.esi.eax', 'esp.edi.esi', '8Bh.8Bh.ebp', 'ecx.edi.edx', 'ebx.esp.ebx', 'esi.ebp.ebp', 'ecx.dl.dl', 'ebp.ebp.esi', 'esi.ecx.edi', 'edx.esp.ecx', 'ebp.esi.edi', 'edi.esp.eax', 'esp.ecx.esi', 'esp.ebx.eax', 'ebx.eax.ecx', 'eax.ecx.ebx', 'esi.ecx.ebx', 'edx.eax.ebx', 'esi.ebx.edi', 'al.ecx.al', 'eax.eax.ax', 'ebx.eax.edx', 'eax.esp.ebp', 'esi.esp.esi', '1.1.1', 'edi.ecx.esi', 'edx.edi.eax', 'ecx.edx.esi', 'ebx.ecx.ebx', 'edx.esi.eax', 'ecx.ebx.eax', 'ax.eax.eax', 'ebp.eax.ebp', 'eax.esi.edx', 'ebx.ebx.esp', 'dl.dl.dl', 'eax.ebx.esp', 'edi.edi.edx', 'ebx.edx.ebx', 'ecx.al.ecx', 'eax.edx.esi', 'edx.ebx.edx', 'eax.ebx.ebp', 'eax.ecx.dl', '49h.49h.49h', 'edx.edx.edi', 'ebp.eax.ecx', 'dl.eax.ebx', 'ecx.edi.esp', 'esi.esi.edx', 'esi.ebx.ebp', '0.0.0', 'ebp.esp.esi', 'esp.eax.esp', 'edx.eax.edi', 'dl.al.eax', 'esp.esp.esp', 'ebx.ebx.edi', 'ecx.ebx.edi', 'ebx.ebp.eax', 'ebp.esp.ebp', 'ebx.ecx.esi', '8Bh.ebp.ebp', 'eax.ecx.esp', 'eax.al.edx', 'esi.ebp.ebx', 'dl.dl.ecx', 'edx.edx.ebx', 'edi.eax.edx', 'ecx.eax.esp']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        register_list = open(file_path, 'r').read().split(',')

        for i in range(len(register_list) - (3 - 1)):
            seq = '.'.join([str(v) for v in register_list[i: i + 3]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_register_4g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/register.txt"

    colnames = ['eax.eax.eax.eax', 'edi.eax.edi.eax', 'ebp.esp.esp.ebp', 'edi.edi.ebp.ebp', 'ebp.ebp.esp.esp', 'eax.esi.ecx.ecx', 'eax.ebp.eax.eax', 'eax.eax.ebp.eax', 'eax.ecx.esi.ecx', 'ecx.ecx.eax.eax', 'ebp.ebp.esp.ecx', 'edi.ebp.ebp.esp', 'ecx.ecx.ecx.ecx', 'eax.edi.eax.edi', 'ecx.ecx.esi.esp', 'eax.ecx.esi.eax', '4.4.4.4', 'ebp.esp.esp.eax', '3Fh.3Fh.3Fh.3Fh', 'eax.edi.eax.ebx', 'ebp.edi.edi.ebp', 'ebp.esp.eax.eax', 'ebx.esp.eax.eax', 'ecx.esi.esp.eax', 'eax.ecx.edi.eax', 'esp.ebp.ebp.eax', 'eax.eax.ecx.ecx', 'eax.eax.ecx.esi', 'eax.eax.edi.esi', 'ecx.ecx.ecx.edi', 'edx.ecx.ecx.edx', 'ecx.ecx.edx.ecx', 'esp.esp.eax.eax', 'eax.eax.eax.edi', 'ecx.ecx.ecx.eax', 'eax.esp.esp.eax', 'eax.edi.esi.ebx', 'eax.ebp.eax.ebx', 'al.al.al.al', 'esp.ebp.ebp.edi', 'esi.ebx.esp.eax', 'eax.ax.edx.eax', 'eax.esp.ebx.esi', 'esp.eax.eax.eax', 'edi.esi.ebx.eax', 'ecx.eax.eax.esi', 'eax.eax.eax.ecx', 'eax.edi.edi.esi', 'eax.ecx.ecx.eax', 'ebx.esi.edi.eax', 'esi.ebx.esp.ebp', 'eax.eax.eax.ebp', 'esi.esp.eax.eax', 'eax.ecx.ecx.ecx', 'edi.esi.ebx.esp', 'eax.eax.esp.ebx', 'esi.eax.eax.esp', '5Fh.5Fh.5Fh.5Fh', 'ecx.eax.eax.ecx', 'ecx.eax.ecx.ecx', 'eax.esi.esp.eax', 'esi.ebx.eax.eax', 'eax.ecx.edi.ecx', 'ecx.esp.eax.eax', 'esi.edi.eax.eax', 'edi.eax.esp.edi', 'ecx.eax.eax.eax', '52h.52h.52h.52h', 'ebp.eax.eax.eax', 'eax.eax.eax.al', 'esi.eax.esi.ebx', 'ebx.ebp.ebp.esp', 'eax.al.al.eax', 'esi.edi.eax.edi', 'eax.esi.eax.edi', 'esp.esi.esi.ecx', 'eax.eax.esp.eax', 'ebx.ebx.ecx.ecx', 'edx.eax.ax.edx', 'eax.esp.eax.eax', 'eax.ebx.eax.eax', 'eax.ebx.ebx.ebx', 'ebx.ebx.eax.eax', 'esi.edi.edi.ebp', 'ecx.edi.eax.eax', 'eax.ebp.ebp.esp', 'ebp.eax.eax.ebx', 'eax.eax.esi.esi', 'esi.esi.esi.esi', 'esi.esi.eax.esi', 'eax.esi.esi.esi', 'eax.eax.ebx.eax', 'ebp.ebp.ebp.esp', 'ebp.ebp.esp.eax', 'eax.eax.eax.esi', 'eax.eax.esi.ecx', 'eax.eax.al.al', 'esi.ecx.ecx.eax', 'edi.edi.eax.eax', 'ebp.esp.esp.ebx']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        register_list = open(file_path, 'r').read().split(',')

        for i in range(len(register_list) - (4 - 1)):
            seq = '.'.join([str(v) for v in register_list[i: i + 4]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list
