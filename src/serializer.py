"""
A simple test program for learning serialization in python using pickle
As a reference: https://realpython.com/python-serialize-data/
"""

import pickle

# keep objects in a data structure. Iterate through the data structure and serialize the objects. Then, you 
# deserialize the data structure, get all of the objects back.

# create a simple data variable
data = 20

#--------------------------------------------------------------------------------------------- SERIALIZING DATA ------------

# open a file with wb mode (writing, binary) and dump the pickled (serialized) data into it.
with open("saves/file.pkl", mode="wb") as file:
    pickle.dump(data, file)                 # dumps writes to a file.

# dumps returns the pickled representation of data as a byte object. This prints out a byte object.
print(pickle.dumps(data))                   # dumps gives us a byte object from an object.

#---------------------------------------------------------------------------------------------- DESERIALIZING DATA ---------

# open a file in read binary mode and load the serialized data into it.
with open("saves/file.pkl", mode="rb") as file:
    a = pickle.load(file)                   # load returns an object from a file

# loads returns the unpickled data. This will print out 20.
print(pickle.loads(b'\x80\x04K\x14.'))      # loads returns an object from a byte object.
print(a)