
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
        return " Error! denominator can't be zero "
 else :
  return "Invalid operation "
 
 return f'The result is {result}'


print(pyCalculator())