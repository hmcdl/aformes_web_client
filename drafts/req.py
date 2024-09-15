import sys
import os
# print (sys.path)
sys.path.append(os.getcwd())
from app.operations import operations
# from .. import main
sessionData = {}
sessionData["token"] = operations.authorise("http://127.0.0.1:8000", username="tester", password="tester")
sessionData["address"] = "http://127.0.0.1:8000"
operations.add_simulation(conver_args_string="aaa",title="job6", filename=r"c:\Work\Dev\simulations_web_cli\starter.py", session_data=sessionData)
# operations.bar(sessionData)
# print(operations.show_my_sims(100, 0, sessionData))
# operations.remove_sim("job7", sessionData)
operations.download_sim("job7", local_dir=r"c:\Work\Dev\simulations_web_cli\drafts", session_data=sessionData)