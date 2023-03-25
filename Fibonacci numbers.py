# ask user for limit of Fibonacci numbers
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# initialize the first two Fibonacci numbers
fib1, fib2 = 0, 1

# generate Fibonacci numbers up to the specified limit
for i in range(n):
    print(fib1)
    fib1, fib2 = fib2, fib1 + fib2
        
      
      
      output:
        Enter the number of Fibonacci numbers to generate: 7
0
1
1
2
3
5
8
