"""
A simple test program for learning serialization in python using pickle
As a reference: https://realpython.com/python-serialize-data/
"""

import pickle

# create a simple data variable
data = 20

# open a file with wb mode (writing, binary) and dump the pickled (serialized) data into it.
with open("saves/file.pkl", mode="wb") as file:
    pickle.dump(data, file)

# dumps returns the pickled representation of data as a byte object. This prints out a byte object.
print(pickle.dumps(data))