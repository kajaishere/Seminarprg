#!/usr/bin/env python3

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def main():
    calculating = True
    result = 0
    num1 = float(input('Enter first number: '))
    while calculating:
        for symbol in operations:
            print(symbol)
        operation = input('Pick an operation: ')
        num2 = float(input('Enter next number: '))
        result = operations[operation](num1, num2)
        print(f'{num1} {operation} {num2} = {result}')
        going = input(f'Type "y" to continue calculating with {result}, type "n" for new calc, type "q" for quit: ').lower()
        if going == 'y':
            calculating = True
            num1 = result
        elif going == 'n':
            calculating = False
            main()
        elif going == 'q':
            calculating = False
            print('Bye')
            exit()

if __name__ == '__main__':
    main()
