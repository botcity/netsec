#
# GeoIP program from "Violent Python" 
# Modified to include option parsing
#

import pygeoip
import optparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def print_record_name(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region_name']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[+] '+str(city)+', '+str(region)+', '+str(country)
    print '[+] Latitude: '+str(latitude)+', Longitude: ' +str(longitude)
    
def print_record_addr(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    time_zone = rec['time_zone']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[+] '+str(city)+', '+str(time_zone)+', '+str(country)
    print '[+] Latitude: '+str(latitude)+', Longitude: ' +str(longitude)

def main():
    title = 'net_geoip_q.py'
    usage = 'usage: %s -H <host IP> -N <host name> [Use -H or -N options. Not both]' % title
    parser = optparse.OptionParser(usage)
    parser.add_option('-H', '--host', dest='host', type='string', help='specify host IP')
    parser.add_option('-N', '--name', dest='name', type='string', help='specify host name')
    (options, args) = parser.parse_args()
    host = options.host
    name = options.name

    
    if (host == None) & (name == None):
        print parser.usage
        exit(0)
    
    elif (name == None):
        print_record_addr(host)
        print '================================'

    elif (host == None):
        print_record_name(name)
        print '================================'

    else:
        print '[!] Invalid options specification'
        print parser.usage
        exit(0)
        
if __name__ == '__main__':
    main()









