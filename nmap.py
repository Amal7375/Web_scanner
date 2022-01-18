import os
import sys
import time

def nmap(ip, option):
    command=('nmap ' +  option+' ' + ip)

    cmd= os.popen(command)


    for i in range(0, 10):
        time.sleep(.1)
        sys.stdout.write('\r' + 'loading' + '*' * i)
        time.sleep(1)

    return cmd.read()

