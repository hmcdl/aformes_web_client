import os
import subprocess
import sys
# sys.path.append(os.getcwd())
# from app import listening_log_socket

ip = "127.0.0.1"
subprocess.call(f'python ./app/listening_log_socket.py {ip}', creationflags=subprocess.CREATE_NEW_CONSOLE)

# ip = requests.get(url="http://127.0.0.1:8000/simulations/ip_echo")
# print(ip.text)
