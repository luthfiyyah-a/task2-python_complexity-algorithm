def generateData():
    number = '0821234567'
    customers = []
    
    for i in range(100):
        if i < 10:
            mobileNumber = number + '0' + str(i)
        else:
            mobileNumber = number + str(i)
            
        customers.append(mobileNumber)
    
    return customers

def sedPromoDiscount(array):
    for i in range(len(array)):
        print('Sending Promo to ' + array[i])
    
    for i in range(10):
        print('Sending Discount to Chosen Customer ' + str(i+1))
        

customers = generateData()
sedPromoDiscount(customers)