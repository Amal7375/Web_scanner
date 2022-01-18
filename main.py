import ip_address
import nmap
import time
import sys

url =input("url to find host ip [ www.example.com / example.com ] :  ")

host_ip = ip_address.ipAdd(url)

print('\n'+'your ip is ' + host_ip)



def verification():

    resp =input('Do you Like to NMAP this host (Y / N) : ')

    if resp == 'Y' or resp == 'y' :
        pass
    elif resp == 'n' or resp == 'N':

        print('QUITTING*****')
        exit('SUCCESS')
    else:
        print('Enter correct value **** ')
        return verification()

verification()

opt=input('enter nmap option to done [ -P is default] : ')

if len(opt) == 0:
    opt = "-P"

rslt = nmap.nmap(host_ip,opt)

print('\n'+rslt)


