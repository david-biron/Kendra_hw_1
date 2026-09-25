import pandas as pd
import sys
import random

assert len(sys.argv)==2

filename=sys.argv[1]
with open(filename, 'r') as file:
    for line in file:
        if random.random()<10/1000:
            print( line )

