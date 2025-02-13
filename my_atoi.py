#https://leetcode.com/problems/string-to-integer-atoi/

def my_atoi(s):
    stripped_s = s.lstrip()
        
    if not stripped_s:
            return 0
        
    sign = ""
    ret_num = ""

    if stripped_s[0] in "+-":
        sign = stripped_s[0]
        stripped_s = stripped_s[1:]

    for el in stripped_s:
        if el.isdigit():
            ret_num += el
        else:
            break
        
    if len(ret_num) > 1 and ret_num.startswith("0"):
        ret_num = ret_num.lstrip("0")
        
    if ret_num:
        result = int(f'{sign}{ret_num}')

        if result < -2**31:
            result = -2**31
        elif result > 2**31-1:
            result = 2**31 -1
        return result
    return 0