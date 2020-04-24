import string

def is_panlindrome_iterative(text):
    left_index = 0 
    right_index = len(text) -1

    # loop
    while left_index < right_index:
        if text[left_index] != text[right_index]: # not a palindrome
            return False
        left_index += 1 
        right_index += 1 
        return True

def recursive_is_palindrome(text, left_index, right_index):
    # print("left", left_index)
    # print("right", right_index)
    # base cases 
    if left_index == right_index or left_index > right_index:
        return True
    if text[left_index] != text[right_index]:
        return False
    # recursive case
    return recursive_is_palindrome(text, left_index+1, right_index-1)

def is_panlindrome(text):
    text = text.lower()
    new_text = ""
    for character in text:
        if character in string.ascii_letters:
            new_text += character

    print(new_text)
    return is_panlindrome_iterative(new_text)

print(is_panlindrome("hello----"))
print(is_panlindrome("AB"))
print(is_panlindrome("Murderforajarofredrum."))
print(is_panlindrome("TACOCAT"))
