#https://leetcode.com/problems/clear-digits/description/

def clear_digits(s):
    res_stack = []

    for element in s:
        if element.isdigit() and not res_stack[-1].isdigit():
            res_stack.pop()
        else:
            res_stack.append(element)

    return "".join(res_stack)
