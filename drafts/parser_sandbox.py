import sys
import os
# 
sys.path.append(os.getcwd())
from app.interface import parsers
print(parsers.parser_add_simulation.print_help())
print(parsers.parser_add_simulation.print_usage())