num1 = 5.27394
num2 = 12.488873
print('num1 is {0} and num2 is {1}'.format(num1, num2))
    # {} uses the index position from format()
print('short num1 is {0:.3} & num2 shows more {1:.3f}'.format(num1, num2))
    # :.* targets the first 3 numbers --- :.*f targets float, first 3 after decimal point
print(f'num1 is {num1:.4} and num2 is {num2:.1f}')
    # using f-strings, simpler way of using .format()