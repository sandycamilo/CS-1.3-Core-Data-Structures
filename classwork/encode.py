import string

# convert 5 to base 2 = 101
# encode (5, 2) -> 101 


#converting base 10 to whatever base we give it 


#loop to do the repeated division, where to stop? 
#get the remainders and divisors 
#save the remainders 
#return the final number result as a string 
#deal with hex digits 


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
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    digits_and_letters = string.digits + string.ascii_letters
    print(digits_and_letters)
    new_number = number
    final_digits = ""
    while new_number != 0:
        remainder = new_number % base 
        if base == 16:
            remainder = digits_and_letters(remainder)
        new_number = new_number // base 
        final_digits += str(remainder)
        
    return final_digits[::-1]


print(encode(5, 2))
print(encode(64206, 16))