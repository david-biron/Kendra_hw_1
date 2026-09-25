import pandas as pd
import sys, random

assert len(sys.argv) == 2

filename = sys.argv[1]
with open(filename, 'r') as file:
    for line in file:
        if random.random()<0.1:
            print(line)

