def arithmetic_arranger(problems, displayMode=False):

  try:
    if len(problems) > 5:
      raise BaseException
  except:
    return "Error: Too many problems."

  start = True
  spacing = "    "
  line1 = line2 = line3 = line4 = ""

  for prob in problems:
    
    sep_prob = prob.split()
    
    num1 = sep_prob[0]
    op = sep_prob[1]
    num2 = sep_prob[2]

    exp = exception_handler(num1, num2, op)
    if exp != "":
      return exp

    n1 = int(num1)
    n2 = int(num2)

    space = max(len(num1), len(num2))

    if start == True:
      line1 += num1.rjust(space + 2)
      line2 += op + ' ' + num2.rjust(space)
      line3 += '-' * (space + 2)
      if displayMode == True:
        if op == '+':
          line4 += str(n1 + n2).rjust(space + 2)
        else:
          line4 += str(n1 - n2).rjust(space + 2)
      start = False

    else:
      line1 += num1.rjust(space + 6)
      line2 += op.rjust(5) + ' ' + num2.rjust(space)
      line3 += spacing + '-' * (space + 2)
      if displayMode == True:
        if op == '+':
          line4 += spacing + str(n1 + n2).rjust(space + 2)
        else:
          line4 += spacing + str(n1 - n2).rjust(space + 2)
  
  if displayMode == True:
    return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    
  return line1 + '\n' + line2 + '\n' + line3



def exception_handler(num1, num2, op):
  
  try:
    int(num1)
  except:
    return "Error: Numbers must only contain digits."
    
  try:
    int(num2)
  except:
    return "Error: Numbers must only contain digits."

  try:
    if len(num1) > 4 or len(num2) > 4:
      raise BaseException
  except:
    return "Error: Numbers cannot be more than four digits."

  try:
    if op != '+' and op != '-':
      raise BaseException
  except:
    return "Error: Operator must be '+' or '-'."
  return ""