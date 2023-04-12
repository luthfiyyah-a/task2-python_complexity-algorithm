import random

telco = ['Telkom', 'Indosat', 'XL', 'Verizon', 'A&T', 'Nippon', 'Vodafone', 'Orange', 'KODI', 'Telefonica', 'T-Mobile']

def findCompany(array, input):
    for i in range(len(array)):
        if array[i] == array[input]:
            print('Company Found : ' + array[input])
            break
        print('Searching Company... ' + str(i+1))
        

company = round(random.random() * 10)
findCompany(telco, company)