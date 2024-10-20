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

def add_simulation(conver_args_string : str, title : str, filename : str, session_data: dict):
    token = session_data["token"]
    headers = {"Authorization": f"Bearer {token}"}
    try:
        request_body = {
            'mdl': ("", open(filename, 'rb')),
        }
    except FileNotFoundError as e:
        print(e)
        return None
    params = {'conver_args_string': conver_args_string, "title": title}
    url = session_data["address"] + "/simulations/add_simulation"
    r = requests.post(url=url, files=request_body, headers=headers, params=params)
    return r.json()

def remove_sim(title: str, session_data: dict):
    token = session_data["token"]
    url = session_data["address"] + "/simulations/remove_sim"
    headers = {"Authorization": f"Bearer {token}", 'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url=url, params={"title": title}, headers=headers)
    return r.json()

def start_simulation(title: str, session_data: dict):
    token = session_data["token"]
    url = session_data["address"] + "/simulations/start_simulation"
    conver_args = {"iters": 1, "simulation": 0, "aeroratio": 1.5}
    ip = requests.get(url=session_data["address"] + "/simulations/ip_echo").json()['ip']
    try:
        subprocess.Popen(f'python ./app/interface/listening_log_socket.py {ip}', creationflags=subprocess.CREATE_NEW_CONSOLE)
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
    a = 0

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

    