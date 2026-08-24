# Activity 4:  Fibonacci Series 

n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n == 0:
    print("No Fibonacci series.")
elif n == 1:
    print("Fibonacci series:")
    print(a)
else:
    print("Fibonacci series:")
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c