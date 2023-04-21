Expression = input(“Please enter an arithmetic expression (e.g. 1 + 2): “)

# Split the expression into its components
X, op, y = expression.split()

# Convert x and y to integers
X = int(x)
Y = int(y)

# Perform the operation based on the operator
If op == “+”:
    Result = x + y
Elif op == “-“:
    Result = x – y
Elif op == “*”:
    Result = x * y
Elif op == “/”:
    Result = x / y

# Output the result as a floating-point value formatted to one decimal place
Print(“{:.1f}”.format(result))

