foods = ['Sate', 'Bakso', 'Dimsum', 'Remes'] #O(1)
drinks = ['Jeruk', 'Teh', 'Kelapa', 'Cendol'] #O(1)

def logPairs(array1, array2, words):
    counter = 0 #O(1)
    for i in range(len(array1)): #O(n)
        for j in range(len(array2)): #O(n+m)
            counter += 1 # (n*m)
            print(words + ' ' + str(counter) + ' ' + array1[i] + ' dan ' + array2[j])


logPairs(foods, drinks, 'Menu')