import time




print('Input 10 numbers')

n1 = input('First number here: ')
n2 = input('Second number here: ')
n3 = input('Third number here: ')
n4 = input('Fourth number here: ')
n5 = input('Fifth number here: ')
n6 = input('Sixth number here: ')
n7 = input('Seventh number here: ')
n8 = input('Eighth number here: ')
n9 = input('Ninth number here: ')
n10 = input('Tenth number here:')




lst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

lst1 = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]




n = len(lst)

for j in range(0,100):
    check = False
    for i in range(0, n-1):
        if int(lst[i]) > int(lst[i + 1]):
            swap = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = swap
            check = True
    if check == False:
        break



print(' ')
print(' ')

print('Original List: ')
for i in range(0, len(lst1)):
    print(lst1[i])

print('--------------------------------------')

print('Number of iterations : ', j, '| Sorted List: ', lst)
time.sleep(20)