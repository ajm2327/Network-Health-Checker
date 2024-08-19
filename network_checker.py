# network_checker.py
import platform
import subprocess

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

def main():
    hosts = ['192.168.0.3', 'google.com', 'github.com']  # Example hosts
    for host in hosts:
        if ping(host):
            print(f'{host} is up!')
        else:
            print(f'{host} is down!')

if __name__ == "__main__":
    main()
