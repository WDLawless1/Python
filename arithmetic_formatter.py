# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:25:13 2020

@author: user
"""

def arithmetic_arranger(problems,statprint = False):
  # Limit of 5 Arithmetic Problems
  if len(problems) > 5:
    return 'Error: Too many problems.'
  # Initialize the output lines.  
  line_1 = ''
  line_2 = ''
  line_3 = ''
  line_4 = ''
  # Parse the problem strings.
  for i, problem in enumerate(problems):
    first, operator, second = problem.split()
    length_1 = len(first)
    length_2 = len(second)
  # Operations are limited to addition and subtraction.
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
  # Operands must only contain digits.
    if not(first.isdigit() and second.isdigit()):
      return 'Error: Numbers must only contain digits.'
  # Operands cannot be more than four digits.
    if (length_1 > 4) or (length_2 > 4):
      return 'Error: Numbers cannot be more than four digits.'
  # Perform the arithmetic operations.
    spacing = max(length_1, length_2) + 2
    if operator == '+':
      result = int(first) + int(second)
    else:
      result = int(first) - int(second)           
  # Right justify the output lines.
    line_1 = line_1 + first.rjust(spacing) 
    line_2 = line_2 + operator + second.rjust(spacing -1)
    line_3 = line_3 + ''.rjust(spacing, '-')
    line_4 = line_4 + str(result).rjust(spacing)
  # Create four spaces on each line to make room for the next problem.
    if i < len(problems) - 1:
      line_1 += '    '  
      line_2 += '    '
      line_3 += '    '
      line_4 += '    ' 
  # Print out the results.
    if statprint:
      arranged_problems = line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip() + '\n' + line_4.rstrip()
    else:
      arranged_problems = line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip()
  print(arranged_problems)
  return arranged_problems
# Test the function.  
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
    
    
