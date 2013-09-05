#
# Simple port scanner
#


import socket

buffer = 'GET / HTTP/1.0'
host = '24.2.2.2' # This string is used to scan a host
tcp_port = [21,22,23,25,80,53,8080,443]  # Array used to specify which TCP ports to scan 
udp_port = [16464,16465,16470,16471] # Array used to specify which UDP ports to scan




# This function doesnt work yet. 
def udp_scan(host, port):
    for p in port:
        print "[+] Scanning port " + str(p)
        try:
            udp_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_conn.connect((host, p))
            print "[+] UDP port " + str(p) + " open on host!!!!! " + str(host)
            udp_conn.close()
            
        except:
            print "[-] UDP port " + str(p) + " closed on host " + str(host)

# TCP scan function.    
def tcp_scan(host, port):
    for p in port:
        print "[+] Scanning port " + str(p)
        try:
            tcp_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp_conn.connect((host, p))
            print "[+] TCP port " + str(p) + " open on host!!!!! " + str(host)
            tcp_conn.close()
            
        except:
            print "[-] TCP port " + str(p) + " closed on host " + str(host)
            

#udp_scan(host, udp_port)
tcp_scan(host, tcp_port)

