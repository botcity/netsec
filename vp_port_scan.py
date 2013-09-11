#
# Port scanner / Banner grabber program from "Violent Python"
#

import optparse
import socket
from threading import *


screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    tgtPort = int(tgtPort)
    data = 'PythonTestCode\r\n'
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send(data)
        results = connSkt.recv(140)
        screenLock.acquire()
        print "[+] %d tcp open **Yay!! :-P " %tgtPort
        if results:    
            print "!!!!Banner grabbed, bitches!!!!"
            print results + "\n"
        else:
            pass
    except:
        screenLock.acquire()
        print "[-] %d tcp closed **Shucks :-( " %tgtPort
        
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    print '[+] Now attempting to resolve DNS for %s' %tgtHost
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" %tgtHost
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Resolve results for: ' + tgtName[0]
    except:
        print '\n[+] Resolve results for: ' + tgtIP
        
    print '[+] Now executing TCP port scan!'
    
    socket.setdefaulttimeout(3)
    for tgtPort in tgtPorts:
        print '[+] Probing TCP port %s' %tgtPort
        t = Thread(target = connScan, args = (tgtHost,tgtPort))
        t.start()
        
        #try:
        #    connScan(tgtHost,tgtPort)
        #except:
        #    print 'Unable to run connScan function'
    

def main():
    title = 'vp_port_scan.py'
    usage = 'usage: %s -H <target host> -p <target port>' % title
    parser = optparse.OptionParser(usage)
    parser.add_option('-H', '--host', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', '--port', dest='tgtPort', type='string', help='specify target port[s], seperated by commas')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(",")
    
    
    if (tgtHost == None) | (tgtPorts[0] == 'None'):
        print parser.usage
        exit(0)
        
    else:
        portScan(tgtHost, tgtPorts)
        
if __name__ == '__main__':
    main()
    
    


