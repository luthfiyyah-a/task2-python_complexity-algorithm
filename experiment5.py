import time

address = 'DKI Jakarta';
addresses = [address] * 1000

def findAddress(addresses):
    tx = time.perf_counter()
    print('The Default Address is ' + (addresses[0]))
    ty = time.perf_counter()
    print('The performance is ' + str((ty-tx)*1000) + ' ms')
    

findAddress(addresses)