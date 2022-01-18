import socket
import sys
import time



def ipAdd(url):

    try:
        ip=socket.gethostbyname(url)
        for i in range(0, 10):
            sys.stdout.write('\r' + 'loading' + '*' * i)
            time.sleep(.5)
        return ip
    except NameError :
    	print('check spelling..')
    	exit()
    except socket.gaierror:
        print('\n''URL not found..')
        exit(':(')

    except Exception :
        print('\nunknown error !!!')
        exit(':(')

















































































































































