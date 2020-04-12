#!python

import string
import sys
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

# TODO: Decode digits from binary (base 2) - binary to base10 
n = input("Enter binary:")
BaseTen = e = 0 
for i in range(len(n)-1, -1, -1):
    BaseTen = BaseTen + int(n[i] * 2 ** e)
    e = e +1 
print(f"Base number is : {BaseTen}")


# TODO: Decode digits from hexadecimal (base 16) - hexa to base10
hexidict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10,'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
hs = 0
hexNum = sys.argv[::-1]
print(len(hexNum))
i = 0 
power = len(hexNum)
while i < len(hexNum):
    hs = hexidict.get(hexNum[i]) * 16 ** (power - 1) + hs
    i +=1 
    power -=1
print(hs)

# TODO: Decode digits from any base (2 up to 36)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)


# TODO: Encode number in binary (base 2)
#base 10 to binary - YES
n = int(input("Enter decimal:"))
bs = ''
while n != 0:
    bs =  bs + str(n % 2)
    n = n//2
print('Binary number is:')
for i in range(len(bs) -1, -1, -1):
    print(bs[i], end= '')

# TODO: Encode number in hexadecimal (base 16)
#base 10 to hexadecimal - YES 
n = int(input("Enter decimal:"))
hs = ''
while n != 0:
    remainder_value = n%16
    if int(remainder_value) ==10:
        hs = hs + 'A'
    elif int(remainder_value) ==11:
        hs = hs + 'B'
    elif int(remainder_value) ==12:
        hs = hs + 'C'
    elif int(remainder_value) ==13:
        hs = hs + 'D'
    elif int(remainder_value) ==14:
        hs = hs + 'E'
    elif int(remainder_value) ==15:
        hs = hs + 'F'
    else:
        hs = hs + str(remainder_value)
    n = n//16
for i in range(len(hs)-1, -1, -1):
    print(hs[i], end= '')

# TODO: Encode number in any base (2 up to 36)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    decoded = decode(digits, base1)
    return encode(decoded, base2)
# TODO: Convert digits from base 2 to base 16 (and vice versa)
# ...
# TODO: Convert digits from base 2 to base 10 (and vice versa)
# ...
# TODO: Convert digits from base 10 to base 16 (and vice versa)
# ...
# TODO: Convert digits from any base to any base (2 up to 36)
# ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
