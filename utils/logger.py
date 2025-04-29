# utils/logger.py
from colorama import Fore, Style

def log_success(ip, user, passwd):
    print(Fore.GREEN + f"[+] Success: {ip} - {user}:{passwd}" + Style.RESET_ALL)
    with open("output/success.json", "a") as f:
        f.write(f'{{"ip": "{ip}", "user": "{user}", "pass": "{passwd}"}},\n')

def log_failure(ip, user, passwd):
    print(Fore.RED + f"[-] Failed: {ip} - {user}:{passwd}" + Style.RESET_ALL)
