class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def pyCalculator() :

 number1 = float(input('Please enter the first number : '))

 operator = input("Enter the operation sign; + or - or * or / : ")

 number2 = float(input('Please enter the second number :  '))

 if operator == '+' :
    result = number1 + number2
 elif operator == '-' :
    result = number1 - number2
 elif operator == '*' :
    result = number1 * number2
 elif operator == '/' :
    if number2 != 0:
      result = number1 / number2
    else:
        return f"{bcolors.FAIL} Error! denominator can't be zero "
 else :
  return f"{bcolors.FAIL}Invalid operation "
 
 return f'{bcolors.OKBLUE} {bcolors.BOLD}The result is {bcolors.UNDERLINE}{result}'


print(pyCalculator())