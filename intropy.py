name = input('What is your name? ')
print('Hello,',name,'!')

name = input('What is your name?')
print((len(name)+4)*'*')
print('*',name,'*')
print((len(name)+4)*'*')

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(a, "+",b,"=",a+b)

a=float(input("Enter the length of the first side: "))
while a<=0:
    print("The length should be positive!")
    a=float(input("Enter the length of the first side: "))
b=float(input("Enter the length of the second side: "))
while b<=0:
    print("The length should be positive!")
    b=float(input("Enter the length of the second side: "))
c=float(input("Enter the length of the third side: "))
while c<=0:
    print("The length should be positive!")
    c=float(input("Enter the length of the third side: "))
if a+b <=c or a+c<=b or b+c<=a:
    print("The input is not correct")
else:
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print("The area of the triangle is ", area)
