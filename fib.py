
# Online Python - IDE, Editor, Compiler, Interpreter
n = int(input('Please enter an integer: '))
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
    
x = fib(n)    
print(x)

