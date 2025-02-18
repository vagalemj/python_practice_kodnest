class PinError(Exception):
    pass

correct_pin = 1234

pin = int(input('Enter 4 digit pin: '))
try:
    if(pin == correct_pin):
        print('Correct Pin')
    else:
        raise PinError('Incorrect Pin')

except PinError as e:
    print('a/c blocked',e)