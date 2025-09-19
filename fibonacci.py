n = int(input("Enter The value for N F series :-"))

a,b = 0,1
count = 0
print("Fibonacci Series :-")
while count < n:
    print(a)
    a,b = b,a+b
    count += 1