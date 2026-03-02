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

class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return self.model + "; " + str(self.year)
    
    def __repr__(self):
        return str(self)


# test for serializing car object.
car = Car("Toyota Corolla", 2011)
car1 = Car("Toyota Sienna", 2010)
car2 = Car("Ford F150", 2021)

car_array = [car, car1, car2]

print(car_array)


# serialize the data.
with open("saves/file.pkl", mode="wb") as file:
    pickle.dump(car_array, file)

# deserialize the car.
with open("saves/file.pkl", mode="rb") as file:
    b = pickle.load(file)

print(b)