def generateData(n):
    baseNumber = '082'
    customers = []
    
    for i in range(n):
        mobileNumber = baseNumber + str(i).zfill(9)
        customers.append(mobileNumber)
    
    return customers

def sedPromoDiscount(input1, input2):
    for i in range(len(input1)):
        print('Sending Promo to ' + input[i])
    
    print('Its Finished to send Promo to ' + str(len(input1)) + ' Customers')
    
    for i in range(len(input2)):
        print('Sending Discount to Chosen Customer ' + str(i+1))
    
    print('Its Finished to send Discount to ' + str(len(input2)) + ' Customers')
    
dataPromo = generateData(100000000)
dataDiscount = generateData(1000)
sedPromoDiscount(dataPromo, dataDiscount)