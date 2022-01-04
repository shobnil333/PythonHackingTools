import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    port_num = int(input('[+] Enter amount of port you want to scan: ').strip())
    print('\n' + '*** Scanning Target --' + '\n')
    for port in range(port_num):
        scan_port(converted_ip, port)
    print('\n' + str(port_num), 'Port scanned Successfully')


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock).decode().strip('\n')
            print('[+] Port', str(port), 'Open', str(banner))
        except:
            print('[+] Port', str(port), 'Is Open')
    except:
        pass


ipaddress = input('[+] Enter Target: ').strip()
scan(ipaddress)
