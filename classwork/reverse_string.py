### function that will reverse a string using a stack ###

def reverse_string(text):
    my_stack = [] # set a stack using a list or array  
                  # only push and pop to the end of the stack (top of the stack); it is more efficient because there's space there.

    for letter in text: 
        my_stack.append(letter) # push to the end

    reversed_string = "" 
    while len(my_stack) != 0: # while stack is not empty
        reversed_string += my_stack.pop(-1) # contatenate each letter on the stack to the string ~ 
                                            # the last letter pushed to stack is the first letter we can access now

    return reversed_string

print(reverse_string("abc"))
