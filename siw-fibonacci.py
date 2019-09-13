how_many = int(input("How many numbers would you like to see?: "))
a = 0
b = 1
fib = 0

for i in range(how_many):
    print("#", i + 1, "a=", a, "b=", b, "fib=", a + b)
    fib = a + b
    a = b
    b = fib