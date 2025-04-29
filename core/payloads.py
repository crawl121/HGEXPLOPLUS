# core/payloads.py

def execute_payload(client, os_type="linux"):
    stdin, stdout, stderr = client.exec_command("whoami && uname -a" if os_type == "linux" else "whoami && systeminfo")
    output = stdout.read().decode()
    print("[*] Payload Output:\n", output)
