num1 = float(input("Enter the first Number: "))
op = input("Enter the operator: ")
if op != "+" or op != "-" or op != "*" or op != "/":
    print("Huzz el")
    exit()
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)  
