import json


def get_api_freq(dir_name):
    # common
    root_path = '../'
    file_name = dir_name + '.vir'

    # change plz
    file_path = root_path + dir_name + "/dll.json"

    colnames = ['isdebuggerpresent', 'getcurrentthreadid', 'unhandledexceptionfilter', 'exitprocess', 'terminateprocess',
                'sleep', 'regclosekey', 'openprocess', 'getcurrentprocess', 'loadlibrarya', 'freelibrary', 'virtualalloc',
                'translatemessage', 'fwrite', 'initializecriticalsection', 'virtualprotect', 'gettickcount', 'waitforsingleobject',
                'setendoffile', 'findclose', 'widechartomultibyte', 'getlasterror', 'lockresource', 'mapviewoffile', 'writefile',
                'multibytetowidechar', 'rtlunwind', 'virtualquery', 'getsysteminfo', 'getprocaddress', 'readfile', 'closehandle',
                'heapdestroy', 'createthread', 'getstdhandle', 'virtualfree', 'fopen', 'getwindowthreadprocessid', 'deletecriticalsection',
                'getcpinfo', 'getlocaltime', 'setfilepointer', 'interlockedincrement', 'getfilesize', 'tlsgetvalue', 'leavecriticalsection',
                'getfiletype', 'heapfree', 'interlockeddecrement', 'releasemutex', 'getoemcp', 'heapcreate', 'createmutexa',
                'entercriticalsection', 'getenvironmentstrings', 'tlssetvalue', 'flushfilebuffers', 'createmutexw', 'setstdhandle',
                'getfilesizeex', 'internetclosehandle', 'exitthread', 'winexec', 'deviceiocontrol', 'isbadreadptr', 'terminatethread',
                'sethandlecount', 'socket', 'createtoolhelp32snapshot', 'internetreadfile', 'getthreadcontext', 'recv', 'wsacleanup',
                'isbadwriteptr', 'connect', 'wsastartup', 'send', 'closesocket', 'virtualallocex', 'openmutexa', 'writeprocessmemory',
                'openfile', 'createremotethread', 'sendto', 'process32next', 'getupdaterect', 'accept', 'gethostname', 'readprocessmemory',
                'setkeyboardstate', 'connectnamedpipe', 'gethostbyaddr', 'process32first', 'bind', 'listen', 'cryptencrypt', 'disconnectnamedpipe',
                'enumprocesses', 'internetwritefile', 'getupdatergn', 'setfileapistoansi', 'internetquerydataavailable', 'internetgetconnectedstate',
                'setfileapistooem', 'icmpsendecho', 'wsasend', 'certdeletecertificatefromstore', 'checkremotedebuggerpresent', 'setfilevaliddata',
                'getbinarytype', 'openfilebyid']

    feature_list = {'hash': file_name}

    for v in colnames:
        feature_list[v] = 0

    try:
        dll = json.loads(open(file_path).read())

        for dll_name in dll:
            for api in dll[dll_name]:
                try:
                    feature_list[api.lower()] += 1
                except:
                    pass

    except:
        pass

    return feature_list
