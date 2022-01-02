import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('[+] Scanning Target --')
    for port in range(1,1000):
        scan_port(converted_ip, port)


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


ipaddress = input('[+] Enter Target: ')
scan(ipaddress)
