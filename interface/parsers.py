import argparse
parser_auth = argparse.ArgumentParser(prog='simulations_web console',
                    description='What the program does',
                    epilog='Levchenkov Mikhail, mihalevch@mail.ru')
parser_auth.add_argument('--connect-to', type=str)
parser_auth.add_argument('--username', type=str)
parser_auth.add_argument('--password', type=str)

parser_add_simulation =  argparse.ArgumentParser(prog='add-simulation',
                    description='This is interactive command for adding new simulation to the DB',
                    epilog='Levchenkov Mikhail, mihalevch@mail.ru')
parser_add_simulation.add_argument('add-simulation')
parser_add_simulation.add_argument('-t', '--title', type=str, required=True)
parser_add_simulation.add_argument('-m', '--mdl', type=str, required=True)
parser_add_simulation.add_argument('-f', '--from-interface', type=str, required=True)
parser_add_simulation.add_argument('-a', '--aeromanual', type=str, required=True)
parser_add_simulation.add_argument('-c', '--control-system', type=str, required=True)


parser_start_sim =  argparse.ArgumentParser()
parser_start_sim.add_argument('start-sim')
parser_start_sim.add_argument('--title', type=str)
parser_start_sim.add_argument('--iters', type=int, default=1)
parser_start_sim.add_argument('--simulation', type=int, default=1)
parser_start_sim.add_argument('--aeroratio', type=float, default=1.5)

parser_remove_sim =  argparse.ArgumentParser()
parser_remove_sim.add_argument('remove-sim')
parser_remove_sim.add_argument('--title', type=str)

parser_show_my_sims =  argparse.ArgumentParser()
parser_show_my_sims.add_argument('show-my-sims')
parser_show_my_sims.add_argument('--limit', type=int, default=100)
parser_show_my_sims.add_argument('--offset', type=int, default=0)

parser_download_sim =  argparse.ArgumentParser()
parser_download_sim.add_argument('download-sim')
parser_download_sim.add_argument('--title', type=str)
parser_download_sim.add_argument('--dir', type=str, required=True)

def parse_args(inp, parser: argparse.ArgumentParser):
    try:
        args = parser.parse_args(inp)
        return args
    except SystemExit:
        print(parser.usage)
