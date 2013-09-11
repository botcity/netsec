#
# Port scanner / Banner grabber program from "Violent Python"
#

import optparse
import socket


def connScan(tgtHost, tgtPort):
    tgtPort = int(tgtPort)
    data = 'PythonTestCode\r\n'
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send(data)
        results = connSkt.recv(1024)
        print "[+] %d tcp open" %tgtPort
        print results
        connSkt.close()
        
    except:
        print "[-] %d tcp closed" %tgtPort

def portScan(tgtHost,tgtPorts):
    print 'Now attempting to resolve DNS for %s' %tgtHost
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
        
    print 'Now executing TCP port scan!'
    for tgtPort in tgtPorts:
        print 'Probing TCP port %s' %tgtPort
        try:
            connScan(tgtHost,tgtPort)
        except:
            print 'Unable to run connScan function'
    

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
        print tgtHost + ":" + str(tgtPorts)
        
if __name__ == '__main__':
    main()
    
    


