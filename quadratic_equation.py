
# Online Python - IDE, Editor, Compiler, Interpreter
import cmath
# This function uses the Quadratic Formula to solve A*X**2 + B*X + C = 0.
def quadratic_roots(a, b, c):
    d = (b ** 2) - (4 * a * c) # d = discriminant
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    return x1, x2

# x1 and x2 are of the complex type.
# The real number domain is the subset of complex numbers whose imaginary parts equal 0.

# Prompt the user to enter the coefficients.
print ('Please enter three coefficients for A*X**2 + B*X + C = 0. ')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))     
print('\n') 
# Test validity of input data. (Is A equal to 0?)
if a == 0: # A = 0, so we solve and print the linear equation B*X + C = 0.
    x1 = None
    x2 = None
    print('This is not a quadratic equation. This is a linear equation,\n', b,' * x + ', c,' = 0, whose solution is: \n\n x = ', -c / b)
else: # A <> 0, so we solve and print the quadratic equation A*X**2 + B*X + C = 0.
   x1, x2 = quadratic_roots(a, b, c)   
   # Let's make the real solutions print out like real numbers.    
   if x1.imag != 0 and x2.imag != 0: # We have two complex solutions.
        print('The complex solutions to the quadratic equation,\n ', a,'*x**2 + ', b,'*x + ', c,' = 0 are: \n\nx = ', x1,' and x = ', x2)
   elif x1 == x2: # We have one unique real solution.
        print('The real solution to the quadratic equation,\n ', a,'*x**2 + ', b,'*x + ', c,' = 0 is: \n\nx = ' + str(x1.real))    
   else: # We have two distinct real solutions.
        print('The real solutions to the quadratic equation,\n ', a,'*x**2 + ', b,'*x + ', c,' = 0 are: \n\nx = ' + str(x1.real) + ' and x = ' + str(x2.real))
    
          
    


        
    
    
     
    
    

