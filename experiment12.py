def generateData(n):
    baseNumber = '082'
    customers = []
    
    for i in range(n):
        mobileNumber = baseNumber + str(i).zfill(9)
        customers.append(mobileNumber)
    
    return customers

def sedPromoDiscount(input):
    for i in range(len(input)):
        print('Sending Promo to ' + input[i])
    
    print('Its Finished to send Promo to ' + str(len(input)) + ' Customers')
    
    for i in range(len(input)):
        print('Sending Discount to Chosen Customer ' + str(i+1))
    
    print('Its Finished to send Discount to ' + str(len(input)) + ' Customers')
    
data = generateData(1000)
sedPromoDiscount(data)