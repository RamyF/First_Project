# validate number
def validateNumber(text):
    while True:
        # cast text to integer
        try:
            text = int(text)
            break
        except ValueError as e:
            print('Error: ', e)
            text = input('Please Enter a numeric value: ')
    return text
# validate a number in a range
def valNumRange(number, rangeLow, rangeHigh):
    while True:
        if number >= rangeLow and number <= rangeHigh:
            return number
        else:
            print('Your selection must be between', rangeLow, 'and', rangeHigh)
            number = input('Please enter a correct value: ')
            number = validateNumber(number)
def validateName(name):
    while True:
        isValid = True
        for char in name:
            if char.isnumeric():
                isValid = False
        if isValid == True:
            break
        print('your name is invalid!')
        name = input('Please Enter a name without numbers or special characters: ')








