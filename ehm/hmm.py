def Hmmm():
    import subprocess
    import time

    cmd = ['xinput', 'list']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()

    print('Output: ' + o)
    ID = []
    ID_M = []


    for line in o.split('\n'):
        if 'keyboard' in line:
            ID.append(line.split('=')[1].split('\t')[0])
            ID_M.append(line.split('(')[1].split(')'))
            print('id=' + ID[-1])
            print('id_master=' + ID_M[-1])

    for id in ID:
        cmd = ['xinput', 'float', id]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        print('Output: ' + o)

    time.sleep(10)

    for id, idm in zip(ID, ID_M):
        cmd = ['xinput', 'reattach', id, idm]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        print('Output: ' + o)

Hmmm()