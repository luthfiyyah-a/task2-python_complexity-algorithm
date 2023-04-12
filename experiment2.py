import time

company = 'telkom'
largeCompanyName = [company] * 1000


def findCompany(array):
    tx = time.perf_counter()
    for i in range(len(array)):
        if array[i] == 'telkom':
            print('company found!');
    
    ty = time.perf_counter()
    print('The performance is ' + str((ty-tx)*1000) + ' ms')
    

findCompany(largeCompanyName)