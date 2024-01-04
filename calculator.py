def  add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1*number2

def divide(number1,number2):
    return number1/number2

operations = {
    '+' : add,
    '-': subtract,
    '*':multiply,
    '/':divide,
}

def calculator():
    number1 = float(input('First Number'))
    
    for operator in operations:
        print(operator)
        
        
    should_continiue = True
    
    while should_continiue:
        operation_symbol = input('What Operation Do You Wanna Do ? (+,-,*,/)')
        
        number2 = float(input('Second Number'))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1,number2)
        
        print(f'{number1} {operation_symbol} {number2} = {answer}')
        
        if input(f'Your Answer: {answer}. Do You Wanna Do More Math? By Typing \'y\' you can continiue or by typing \'n\' you can restart. ') == 'y':
            number1 = answer
        else:
            should_continiue = False
            calculator()        
            
calculator()