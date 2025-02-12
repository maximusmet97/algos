#https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

def max_sum(nums):
    sum_tables = {}
    sums = []

    for idx in range(0,len(nums)):
        divided_num = [int(x) for x in list(str(nums[idx]))] 
        sum_of_digits = sum(divided_num)
         
        if not sum_of_digits in sum_tables.keys():
            sum_tables[sum_of_digits] = [nums[idx]]
        else:
            sum_tables[sum_of_digits].append(nums[idx])
     
     for val in sum_tables.values():
        if len(val) > 1:
            val.sort(reverse=True)
            sums.append(val[0]+val[1])

     if sums:
         return max(sums)

      return -1
