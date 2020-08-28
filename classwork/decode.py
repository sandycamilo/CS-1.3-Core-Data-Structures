#TODO: how do we solve this problem by hand?
#Take each digit 
#we find the position of each digit
#we multiply the digit by the base raised to the power of the position
#add all these results together

#given a string, I need to break apart the digit string into individual digits or characters
#.split()?
#right to left, rightmost is 0, reverse digits? .reverse()
#get a for loop and get each digit position
# 1 0 1
#counter 

#What coding constructs would help up replicate this in code?

#example input and output
#decode(101, 2) -> 5
def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # TODO: Decode digits from hexadecimal (base 16)
    # TODO: Decode digits from any base (2 up to 36)
    digits = digits[::-1] #reverse the digit string
    sum = 0 # set a counter 
    for i in range(len(digits)): # for digit in the digits 
        result = int(digits[i]) * base ** i # set result = digit in string * base^exponent 
        sum += result # add result to accumulative sum 
    return sum 

print(decode('101', 2))#expect to see 5