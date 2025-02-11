#https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

def remove_occurences(string,part):
    substr_len = len(part)
    stack_str = ""

    for letter in string:
        stack_str += letter

        if part in stack_str and stack_str[len(stack_str)-substr_len:] == part:
            stack_str = stack_str[:len(stack_str)-substr_len]

    return stack_str
