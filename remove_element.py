#https://leetcode.com/problems/remove-element/description

def remove_element(nums,val):
    write_idx = 0
        
    for read_idx in range(0,len(nums)):
        if nums[read_idx] != val:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
        
    return write_idx    
