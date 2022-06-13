#def add (x, y):
#    return x + y
#def subtract (x, y):
#    return x - y
#def multiply (x, y):
#    return x * y
#def exponent (x, y):
#    return x ** y
#def divide (x, y):
#    return x / y
#def wholeDivide (x, y):
#    return x // y
#def modulo (x, y):
#    return x % y
#
## printing a control menu for the user to interact with
#print('What method will thy use to calculate sword quantities?')
#print('add')
#print('subtract')
#print('multiply')
#print('exponent')
#print('divide')
#print('wholeDivide')
#print('modulo')
#
## functionality of the control menu - where user may interact with the menu to use the arithmetic operators defined previously in the script
#while True:
#    #take input from user
#    choice = input("Type in choice: ")
#    #check if the choice is valid
#    if choice in ('add', 'subtract', 'multiply', 'exponent', 'divide', 'wholeDivide', 'modulo'):
#        num1 = float(input('Enter First Number: '))
#        num2 = float(input('Enter Second Number: '))
#
#    if choice == 'add':
#        print('{} + {} = '.format(num1, num2))
#        print(num1 + num2)
#
#    elif choice == 'subtract':
#        print('{} - {} = '.format(num1, num2))
#        print(num1 - num2)
#
#    elif choice == 'multiply':
#        print('{} * {} = '.format(num1, num2))
#        print(num1 * num2)
#
#    elif choice == 'divide':
#        print('{} / {} = '.format(num1, num2))
#        print(num1 / num2)