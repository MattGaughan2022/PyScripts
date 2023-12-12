import pickle

vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year' : 2015,
    'color': 'Black Sapphire'
}

my_file = open('vehicledetail.bin', 'wb')
pickle.dump(vehicle, my_file)
my_file.close()

with open('cooking.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print("Vehicle details - ")
print(vehicle)