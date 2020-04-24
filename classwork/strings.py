# "execputecute" "cute"

def find_all_indexes(text,pattern): 
    all_indexes = [] # list to store indexes where the start of the pattern is found

    if pattern == "": # handles empty string test case - 
        for i in range(len(text)):
            all_indexes.append(i)
        return all_indexes # return all because every string/substring contains the empty string

    for text_index in range(len(text)): 
        letter = text[text_index] # each letter in the text
        if letter == pattern[0]: # check if each of those letters is the start of the pattern
            for pattern_index in range(len(pattern)): # then we keep checking the rest of the pattern and the rest of the text to see if rest of pattern is present
                if pattern[pattern_index] != text[text_index + pattern_index]: # where we started in the text + where we are looking in the rest of the pattern
                    break # if there is a mismatch we break 
                # if we hit the end of the pattern and we did not break then we append the index and say we found the pattern
                if pattern_index == len(pattern) -1:
                    all_indexes.append(text_index)
    return all_indexes

print(find_all_indexes('aaa', 'a'))
print(find_all_indexes('abcabcdabcde','abcd'))
print(find_all_indexes('abcabcabcde', ''))