add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a*b
divide = lambda a, b: a/b if b != 0 else "Error: Division by zero"

if __name__ == "__main__":
    
    x, y = 4, 2
    print(f"Add: {x} + {y} = {add(x, y)}")
    print(f"Subtract: {x} - {y} = {subtract(x, y)}")
    print(f"Multiply: {x} * {y} = {multiply(x, y)}")
    print(f"Divide: {x} / {y} = {divide(x, y)}")
