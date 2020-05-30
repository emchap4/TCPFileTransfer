import threading
import socket
import os

'''
TODO: Add metadata send first (establish connection)
'''

'''
@return str client's IP address
'''
def get_ip_addr():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr

class Listener:
    '''
    Creates listener thread which calls nc (TCP) listener 
    '''
    def __init__(self, port, file):
        self.port = str(port)
        self.file = file

    def run(self):
        #Runs the nc listener 
        os.system("nc -l " + self.port + " > " + self.file)


class Sender:
    '''
    Creates sender thread
    '''
    def __init__(self, port, file, ip):
        self.port = port 
        self.ip = ip
        self.file = file

    def run(self):
        #Runs the nc sender
#        os.system("cat " + self.file + " | nc " + self.ip + " 6667")
        os.system("cat " + self.file + " | nc " + self.ip + " 6667")

if __name__ == "__main__":
    selection = int(input("Listener[1], Sender[2]"))
    if selection == 1:
        lis = Listener("6667", "dump.txt")
        lis.run()
    elif selection == 2:
        sen = Sender("6667", "sender.txt", "192.168.28.122")
        sen.run()
