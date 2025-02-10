#https://leetcode.com/problems/add-binary/description/

def add_binary(bin_a,bin_b):
    result = "" 
    remainder = 0

    max_len = max(len(bin_a), len(bin_b))
    bin_a_cpy, bin_b_cpy = bin_a.zfill(max_len), bin_b.zfill(max_len)

    for idx in range(max_len-1, -1, -1):
            
        upper = int(bin_a_cpy[idx])
        lower = int(bin_b_cpy[idx])
        sum = upper ^ lower ^ remainder

        if (upper == 1 or lower == 1 or remainder == 1) and (sum == 0):
            remainder = 1
        elif (upper == 1 and lower == 1 and remainder == 1):
            remainder = 1
        else:
            remainder = 0
        result += str(sum)
        
    if remainder != 0:
        result += str(remainder)
    return result[::-1]   


print(add_binary("1111","1111"))

