#https://leetcode.com/problems/reverse-integer/

def reverse_integer(x):
    x_as_str = str(x)
    res_str = x_as_str[::-1]
    res_str_int = None

    if "-" in x_as_str:
        x_as_str = x_as_str.replace("-", "")
        res_str_int = int(f'-{x_as_str[::-1]}')
    else:
        res_str_int = int(res_str)

    if res_str_int > 0 and res_str_int.bit_length() >= 32 or res_str_int < 0 and res_str_int.bit_length() >= 32:
        return 0
        
    return res_str_int
