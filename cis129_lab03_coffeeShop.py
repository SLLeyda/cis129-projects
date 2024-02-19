#CIS 129 Lab 3
#Scott Leyda

#gain input from the user
x=input('How many cups of coffee would you like?')
v=input('How many cups of tea would you like?')
y=input('How many muffins would you like?')
z=input('How many biscotti would you like?')

#calculate costs
x=int(x)
v=int(v)
y=int(y)
z=int(z)
a=x*5
c=v*4
b=y*4
d=z*5
e=(a+b+c+d)*.06
subtotal=a+b+c+d
total=a+b+c+d+e

#print receipt
print('******************************')
print('My Coffee and Muffin Shop')
print('Number of Coffees Bought?')
print(x)
print('Number of Teas Bought?')
print(v)
print('Number of Muffins Bought?')
print(y)
print('Number of Biscotti Bought?')
print(z)
print('******************************')
print()
print()
print('******************************')
print(x,'Coffee at $5 each:','$',a)
print(v,'Tea at $4 each:','$',c)
print(y,'Muffins at $4 each:','$',b)
print(z,'Biscotti at $5 each:','$',d)
print('6% Tax:','&',e)
print('------------')
print('Total:','$',total)
print('******************************')
