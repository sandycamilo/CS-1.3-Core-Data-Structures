
def check_brackets(expression):
    # push open on stack
    # if find an end compare to top of strack
    open_bracket = "{[("
    closed_bracket = "}])"
    bracket_stack = [] 

    for character in expression: # grab each character in string
        if character in open_bracket: 
            bracket_stack.append(character) # push it to stack 
        if character in closed_bracket:
            if len(bracket_stack) == 0:
                return False

            position = closed_bracket.index(character)

            open_bracket_at_top = bracket_stack.pop(len(bracket_stack) - 1)
            #check if the open bracket at the top matches the closed bracket
            if open_bracket_at_top != open_bracket[position]:
                return False

    if len(bracket_stack) == 0:
        return True
    else:
        return False

print(check_brackets("[[hello]], ((how are you))"))
print(check_brackets("[[hello]], ((how are you)"))
print(check_brackets("[[hello]], ((how are you))("))
print(check_brackets("[hello]], ((((how are you))"))
