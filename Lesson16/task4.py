def add(l, r):
    return l + r

def subtract(l, r):
    return l - r

def multiply(l, r):
    return l * r

math_operations = [
    add,
    subtract,
    multiply,
    ]

def perform_operation(op_functions, op_name, l, r):
    for f in op_functions:
        if f.__name__ == op_name:
            return f(l, r)

print(perform_operation(math_operations, 'add', 1, 2))
print(perform_operation(math_operations, 'subtract', 1, 2))
print(perform_operation(math_operations, 'multiply', 1, 2))
