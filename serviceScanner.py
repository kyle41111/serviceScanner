#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))

    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_service_name()




remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)


print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60


t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()


t2 = datetime.now()


total =  t2 - t1


print 'Scanning Completed in: ', total
