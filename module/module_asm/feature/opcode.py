def get_opcode_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/opcode.txt"

    colnames = ['pop', 'call', 'add', 'test', 'xor', 'and', 'mov', 'sub', 'push', 'retn', 'jnz', 'jz', 'jmp', 'movzx',
                'leave', 'jle', 'dec', 'not', 'rol', 'inc', 'xchg', 'lea', 'imul', 'neg', 'pushf', 'nop', 'div', 'std',
                'sbb', 'movsb', 'bt', 'fild', 'clc', 'setnl', 'cmpsb', 'setb', 'int', 'shld', 'jo', 'fdivp', 'fstcw',
                'cmpsd', 'setle', 'outsd', 'bsr', 'scasw', 'aas', 'rdtsc', 'aad', 'loope']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        opcode_list = open(file_path, 'r').read().split(',')

        for op in opcode_list:
            try:
                feature_list[op] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_opcode_1g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/opcode.txt"

    colnames = ['call', 'pop', 'add', 'mov', 'xor', 'retn', 'or', 'test', 'push', 'jmp', 'cmp', 'jz', 'sub', 'jnz', 'jb', 'and', 'dec', 'shr', 'inc', 'jle', 'lea', 'movzx', 'leave', 'js', 'rol', 'ja', 'not', 'xchg', 'imul', 'jl', 'jnb', 'shl', 'setz', 'jns', 'neg', 'jge', 'movsx', 'pushf', 'jbe', 'nop', 'stosd', 'adc', 'jg', 'sar', 'pusha', 'sbb', 'wait', 'setnz', 'sahf', 'movsb', 'movsd', 'cdq', 'div', 'scasb', 'fnclex', 'idiv', 'clc', 'bt', 'mul', 'setnle', 'fild', 'fld', 'cmc', 'faddp', 'popa', 'fstp', 'fnstsw', 'fldcw', 'fmul', 'cmpsb', 'xadd', 'int', 'fsubp', 'fcomp', 'ror', 'shrd', 'fmulp', 'jo', 'fadd', 'fldz', 'setl', 'callvirt', 'ldarg.1', 'fdiv', 'fsub', 'stloc.0', 'cvtps2pd', 'in', 'bts', 'fsubr', 'shld', 'endfinally', 'ldloc.1', 'fst', 'movdqa', 'bswap', 'stloc.1', 'jp', 'cmovnz', 'ldarg.0']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        opcode_list = open(file_path, 'r').read().split(',')

        for op in opcode_list:
            try:
                feature_list[op] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_opcode_2g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/opcode.txt"

    colnames = ['.', 'retn.', 'mov.mov', 'push.call', 'call.pop', 'jmp.', 'push.retn', '.mov', 'mov.push', 'call.call', 'jz.push', 'push.push', 'inc.push', 'add.mov', 'mov.test', 'mov.jmp', 'xor.call', 'jz.test', 'push.mov', 'mov.or', 'mov.call', 'xor.pop', 'jmp.mov', 'test.jz', 'push.sub', 'pop.pop', 'or.jz', 'pop.retn', 'mov.jnz', 'call.mov', '.jmp', 'add.retn', 'mov.pushf', 'add.jmp', 'mov.retn', 'jz.mov', 'add.test', 'mov.add', 'lea.cmp', 'call.add', 'jmp.jmp', 'mov.jz', 'leave.retn', 'xor.cmp', 'pop.mov', 'sub.mov', 'jz.pop', 'cmp.jb', 'pop.push', 'dec.jnz', 'mov.pop', 'test.jnz', 'pop.leave', 'jnz.push', 'lea.test', 'mov.xor', 'jnz.cmp', 'pop.inc', 'retn.mov', 'call.xor', 'mov.jg', 'inc.dec', 'sub.sub', '.pop', 'jz.jmp', 'inc.mov', 'movzx.inc', 'pop.jz', 'cmp.jz', 'mov.sub', 'retn.pop', 'jz.cmp', 'pop.test', 'mov.lea', 'xor.mov', 'retn.push', 'call.', 'lea.mov', 'lea.jmp', 'lea.push', 'jnz.mov', '.push', 'cmp.jnz', 'add.sub', 'call.push', 'pop.sub', 'xor.retn', 'xor.jmp', 'mov.inc', 'jmp.push', 'test.mov', 'test.js', 'retn.jmp', 'movzx.shl', 'cmp.pop', 'or.mov', 'js.mov', 'sub.push', 'xor.inc', 'add.cmp']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        opcode_list = open(file_path, 'r').read().split(',')

        for i in range(len(opcode_list) - (2 - 1)):
            seq = '.'.join([str(v) for v in opcode_list[i: i + 2]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_opcode_3g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/opcode.txt"

    colnames = ['..', 'jmp..', 'retn..', '..jmp', '..mov', 'push.push.push', '.mov.push', 'push.push.call', 'mov.mov.mov', 'mov.push.call', 'jz.mov.push', 'call.add.test', 'ret..ldarg.0', 'lea.sub.push', 'call.ret.', 'ret..', 'push.retn.', 'mov.push.push', '..push', 'mov.jmp.', 'mov.add.mov', '.ldarg.0.call', 'add.cmp.jb', 'ldarg.0.call.ret', 'jmp.mov.lea', 'jz.call.add', 'mov.test.jz', 'mov.add.jmp', 'call.push.call', 'add.jmp.mov', 'add.retn.', 'mov.push.retn', 'ldloc.0.ret.', 'xor.pop.retn', 'lea.jmp.lea', 'xor.push.lea', 'push.call.call', 'jmp.jmp.jmp', '..ldarg.0', 'mov.jnz.mov', '.mov.retn', 'add.mov.add', 'mov.lea.mov', 'call.call.call', 'jz.push.push', 'retn..mov', 'test.jz.pop', 'jz.test.jz', 'push.call.mov', 'call.stloc.s.ldloc.s', 'lea.jmp.mov', 'add.mov.test', 'pop.push.push', 'push.mov.call', 'push.push.mov', 'mov.mov.jmp', 'push.call.pop', 'jmp..mov', 'pop.leave.retn', 'add.mov.mov', 'mov.mov.push', 'call.test.js', 'jmp..sub', 'jz.mov.test', 'mov.push.sub', 'lea.push.push', 'pop.pop.retn', 'push.mov.push', 'mov.mov.test', '.jmp.', 'mov.retn.', 'test.jz.cmp', 'mov.jmp.mov', 'test.mov.jz', 'push.call.push', 'call.xor.push', 'jmp.push.mov', 'call.cmp.mov', 'pop.pop.pop', 'call.retn.', 'jnz.mov.mov', 'xor.inc.retn', 'call.mov.add', 'add.test.jz', 'cmp.jz.push', 'test.jz.push', 'jnz.mov.test', 'call.push.push', 'jmp..lea', 'add.push.call', 'push.sub.push', 'jmp.mov.mov', 'mov.mov.add', 'mov.xor.call', 'cmp.jnz.mov', '.push.mov', 'retn.push.mov', 'pop.retn.mov', 'jnz.mov.jmp', 'call.test.jz']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        opcode_list = open(file_path, 'r').read().split(',')

        for i in range(len(opcode_list) - (3 - 1)):
            seq = '.'.join([str(v) for v in opcode_list[i: i + 3]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list


def get_opcode_4g(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/opcode.txt"

    colnames = ['...', 'jmp...', 'retn...', 'ret...', 'ret..ldarg.0.call', 'retn..mov.push', 'ldarg.0.call.ret.', '...jmp', 'push.call.add.test', '...ldarg.0', '...push', 'push.push.push.call', 'call.add.test.jz', 'push.push.push.push', 'jz.push.call.add', 'add.retn..mov', 'mov.mov.mov.mov', 'mov.push.push.push', 'add.mov.add.mov', 'jmp.mov.add.jmp', 'call.ret..ldarg.0', 'mov.add.mov.add', 'push.retn..', 'jmp..mov.push', 'mov.add.jmp.mov', 'add.jmp.mov.add', 'cmp.jnz.mov.mov', '.mov.push.mov', 'jmp.mov.lea.mov', 'lea.mov.mov.push', 'call.add.mov.test', '..push.mov', 'jz.push.push.push', 'cmp.jz.test.jz', 'push.push.call.pop', 'mov.retn..mov', 'lea.jmp.mov.lea', 'ret..ret.', 'mov.mov.push.push', 'push.call.push.push', 'jz.mov.push.push', 'pop.retn..mov', 'call.pop.pop.test', 'mov.mov.add.mov', 'jmp.jmp.jmp.jmp', 'add.mov.mov.add', 'lea.push.lea.call', 'lea.jmp.lea.jmp', 'mov.jmp..mov', 'push.call.push.call', 'jnz.mov.cmp.jz', 'test.jz.push.push', 'push.mov.call.mov', 'call.mov.jmp.', 'jmp.mov.add.mov', 'add.retn..push', 'call.call.call.call', 'jz.mov.mov.push', 'pop.pop.pop.retn', 'push.mov.call.jmp', 'add.test.jz.mov', 'mov.test.jz.mov', 'mov.add.mov.mov', '..jmp.', 'add.mov.mov.mov', 'push.push.call.push', 'push.push.mov.call', 'push.push.call.mov', 'jnz.mov.push.push', 'mov.push.sub.push', 'pop.pop.pop.pop', 'test.jnz.push.push', 'mov.mov.test.jz', 'mov.cmp.jz.xor', 'push.mov.add.mov', 'mov.jmp.mov.mov', 'test.mov.jz.mov', 'push.push.push.mov', 'lea.mov.xor.call', 'push.call.pop.pop', 'call.test.mov.jz', 'ret..ldarg.0.ldarg.1', 'push.call.mov.cmp', 'push.call.mov.add', 'push.push.mov.mov', 'mov.call.mov.test', '.ret..ret', 'push.mov.call.test', 'lea.push.push.push', 'jz.mov.test.jz', 'push.call.pop.test', 'jmp..mov.jmp', 'push.mov.call.push', 'xor.push.lea.mov', 'ldarg.0.ldarg.1.stfld.ret', 'push.push.call.add', 'mov.mov.mov.add', '.mov.retn.', 'mov.pop.retn.', 'ldarg.1.stfld.ret.']

    # Opcode List Info
    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        opcode_list = open(file_path, 'r').read().split(',')

        for i in range(len(opcode_list) - (4 - 1)):
            seq = '.'.join([str(v) for v in opcode_list[i: i + 4]])

            try:
                feature_list[seq] += 1
            except:
                pass

    except:
        pass

    return feature_list
