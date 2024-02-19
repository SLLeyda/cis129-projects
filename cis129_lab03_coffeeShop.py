#CIS 129 Lab 3
#Scott Leyda

#gain input from the user
x=input('How many cups of coffee would you like?')
y=input('How many muffins would you like?')

#calculate costs
x=int(x)
y=int(y)
a=x*5
b=y*4
c=(a+b)*.06
subtotal=a+b
total=a+b+c

#print receipt
print('******************************')
print('My Coffee and Muffin Shop')
print('Number of Coffees Bought?')
print(x)
print('Number of Muffins Bought?')
print(y)
print('******************************')
print()
print()
print('******************************')
print(x,'Coffee at $5 each:','$',a)
print(y,'Muffins at $4 each:','$',b)
print('6% Tax:','&',c)
print('------------')
print('Total:','$',total)
print('******************************')
