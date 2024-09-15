import os
import subprocess
import sys

import requests
sys.path.append(os.getcwd())
from app.interface import listening_log_socket

# ip = "127.0.0.1"
# subprocess.call(f'python ../app/listening_log_socket.py {ip}', creationflags=subprocess.CREATE_NEW_CONSOLE)

ip = requests.get(url="http://127.0.0.1:8000/simulations/ip_echo")
ip_text = ip.json()['ip']
print(ip.text)
a = 0
