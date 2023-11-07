from sys import argv, exit
from os.path import isfile
import pandas as pd
import manipulator
import gui

path = " ".join(argv[1:])
if not isfile(path):
    print("Please provide the path to the data!")
    exit(1)

print("Loading data")
try:
    data = pd.read_csv(path)
except Exception as e:
    print("Failed to load data:", e)
    exit(2)

print("Manipulating data")
# TODO

gui.open_gui(data)
print("Exiting")