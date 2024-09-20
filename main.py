import sys
import argparse
import requests
import shlex
import json
from interface import parsers
from operations import operations



if __name__ == "__main__":
    session_data = {}
    args = parsers.parser.parse_args()
    session_data["token"] = operations.authorise(args.connect_to, username=args.username, password=args.password)
    session_data["address"] = args.connect_to
    # s = "--show-my-sims --limit 100 --offset 0"
    while True:
        # inp = "--show-my-sims --limit 100 --offset 0"
        inp = input('$: ')

        # args_list = sys.argv[1:]
        
        # print(shlex.split(inp))
        inp = shlex.split(inp)
            # print(session_data["token"])
        if inp[0] == "show-my-sims":
            args = parsers.parse_args(parser=parsers.parser_show_my_sims, 
                                      inp=inp)
            # args = parsers.parser_show_my_sims.parse_args(inp)
            result = operations.show_my_sims(args.limit, args.offset, session_data=session_data)
            print(json.dumps(result, indent=2))
        elif inp[0] == "add-simulation":
            args = parsers.parse_args(parser=parsers.parser_add_simulation, 
                                      inp=inp)
            if args == None:
                continue
            result = operations.add_simulation(
                title=args.title, 
                mdl=args.mdl,
                from_interface=args.from_interface,
                control_system=args.control_system,
                aeromanual=args.aeromanual,
                session_data=session_data)
            print(json.dumps(result, indent=2))
        elif inp[0] == "remove-sim":
            args = parsers.parse_args(parser=parsers.parser_remove_sim, 
                                      inp=inp)
            if args == None:
                continue
            result = operations.remove_sim(
                title=args.title, session_data=session_data)
        elif inp[0] == "start-sim":
            args = parsers.parse_args(parser=parsers.parser_start_sim, 
                                      inp=inp)
            if args == None:
                continue
            result = operations.start_simulation(
                title=args.title, 
                iters=args.iters,
                simulation=args.simulation,
                aeroratio=args.aeroratio,
                session_data=session_data)
            print(json.dumps(result, indent=2))
        elif inp[0] == "download-sim":
            args = parsers.parse_args(parser=parsers.parser_download_sim, 
                                      inp=inp)
            if args == None:
                continue
            result = operations.download_sim(
                title=args.title, 
                local_dir=args.dir,
                session_data=session_data)
            print(json.dumps(result, indent=2))
        else:
            print('unknown argument options')
              
