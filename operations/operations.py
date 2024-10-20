from pathlib import Path
import requests
import json
import os 
import subprocess
# from requests_toolbelt.multipart.encoder import MultipartEncoder

def authorise(address : str, username: str, password: str) -> str:
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {"grant_type": "password", "username": username, "password": password}
    r = requests.post(url=address + '/token', data=data, headers=headers)
    return r.json()["access_token"]

def show_my_sims(limit: int, offset: int, session_data: dict):
    token = session_data["token"]
    headers = {"Authorization": f"Bearer {token}"}
    data = {"limit": limit, "offset": offset}
    r = requests.get(url=session_data["address"] + '/simulations/show_my_sims', data=data, headers=headers)
    return r.json()

def add_simulation(title : str, mdl : str,
                   aeromanual: str, from_interface: str, 
                   control_system: str, session_data: dict):
    token = session_data["token"]
    headers = {"Authorization": f"Bearer {token}"}
    try:
        request_body = {
            'mdl': ("", open(mdl, 'rb')),
            'aeromanual': ("", open(aeromanual, 'rb')),
            'from_interface': ("", open(from_interface, 'rb')),
            'control_system': ("", open(control_system, 'rb')),
            
        }
    except FileNotFoundError as e:
        print(e)
        return None
    params = {"title": title}
    url = session_data["address"] + "/simulations/add_simulation"
    r = requests.post(url=url, files=request_body, headers=headers, params=params)
    return r.json()

def remove_sim(title: str, session_data: dict):
    token = session_data["token"]
    url = session_data["address"] + "/simulations/remove_sim"
    headers = {"Authorization": f"Bearer {token}", 'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url=url, params={"title": title}, headers=headers)
    return r.json()

def start_simulation(title: str, session_data: dict, iters, simulation, aeroratio):
    token = session_data["token"]
    url = session_data["address"] + "/simulations/start_simulation"
    conver_args = {"iters": iters, "simulation": simulation, "aeroratio": aeroratio}
    ip = requests.get(url=session_data["address"] + "/simulations/ip_echo").json()['ip']
    try:
        log_socket_abs_path = os.path.abspath(os.path.join(Path(__file__).parent, "listening_log_socket.py") )
        subprocess.Popen(f'python {log_socket_abs_path} {ip}', creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        print( "error with listening_log_socket")
    r = requests.post(url=url, params={"title": title}, json=conver_args, headers={"Authorization": f"Bearer {token}"})
    
    return r.json()

def download_sim(title: str, local_dir: str,  session_data: dict):
    token = session_data["token"]
    url = session_data["address"] + "/simulations/download"
    r = requests.get(url=url, params={"title": title}, headers={"Authorization": f"Bearer {token}"})
    print(r.content)
    print(r.headers)
    with open(os.path.join(local_dir, title + '.zip'), "wb") as f:
        f.write(r.content)
    return {"status" : "success"}

def bar(session_data):
    token = session_data["token"]
    headers = {"Authorization": f"Bearer {token}"}
    reques_body = {
    # 'mdl': open(r"c:\Work\Dev\simulations_web_cli\starter.py", 'rb'),
    'k': (None, 666),
    'd': (None, 777),
    'mdl':  open(r"c:\Work\Dev\simulations_web_cli\starter.py", 'rb')
    }
    # data = json.loads(json.dumps(data))
    r = requests.post(url=session_data["address"] + "/simulations/foo", files=reques_body, headers=headers)
    return r.json()
    # HTML Form URL Encoded: application/x-www-form-urlencoded

    