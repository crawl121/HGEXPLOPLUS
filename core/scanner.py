# core/scanner.py
import socket

def is_ssh_open(ip, port=22, timeout=2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        banner = s.recv(1024).decode()
        s.close()
        return True, banner
    except:
        return False, None

def scan_targets(ip_list, port=22):
    alive = []
    for ip in ip_list:
        ok, banner = is_ssh_open(ip, port)
        if ok:
            alive.append((ip, banner))
    return alive
